import bpy
import re
import time
from contextlib import redirect_stdout

bl_info = {
    'name': 'TransMat',
    'category': 'Node Editor',
    'author': 'Spectral Vectors',
    'version': (0, 2, 7),
    'blender': (2, 90, 0),
    'location': 'Node Editor',
    "description": "Automatically recreates Blender materials in Unreal"
}

################################################################################
# Directory Code
################################################################################

class TransmatPaths(bpy.types.PropertyGroup):
    
    exportdirectory : bpy.props.StringProperty(
        name = "Export",
        description = "Path where the .py will be saved",
        default = "",
        subtype = 'DIR_PATH'
    )
    
    materialdirectory : bpy.props.StringProperty(
        name= "Material",
        description="Subfolder to save Materials to",
        default = "Materials"
    )
    
    texturedirectory : bpy.props.StringProperty(
        name= "Texture",
        description="Subfolder to save Textures to",
        default = "Textures"
    )
    
    noiseresolution: bpy.props.IntProperty(
        name="Resolution",
        description="Resolution of the baked noise textures",
        default=1024
    )

################################################################################
# Noise Node Baking
################################################################################

class BakeNoises(bpy.types.Operator):
    """Bakes procedural noise nodes to textures for export"""
    bl_idname = "blui.bakenoises_operator"
    bl_label = "Bake Noise Nodes"
    
    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.type == 'NODE_EDITOR'

    def execute(self, context):
        
        previousrenderengine = bpy.context.scene.render.engine
        material = bpy.context.material
        nodes = material.node_tree.nodes
        links = material.node_tree.links
        noisenodes = []
        
        bpy.context.scene.render.engine = 'CYCLES'
        bpy.context.scene.cycles.device = 'GPU'
        bpy.context.scene.cycles.samples = 128
        
        for node in nodes:
            if node.bl_idname.startswith("ShaderNodeTex") and not node.bl_idname == "ShaderNodeTexImage":
                noisenode = node
                noisenodes.append(noisenode)
            if node.bl_idname == "ShaderNodeOutputMaterial":
                output = node
                
        for noisenode in noisenodes:
            for link in noisenode.outputs[0].links:
                nnlinksocket = link.to_socket
                        
            noisebake = bpy.data.images.new(name=str(noisenode.name).replace('.','_').replace(' ',''), width=context.scene.transmatpaths.noiseresolution, height=context.scene.transmatpaths.noiseresolution)
            
            bpy.ops.node.add_node(type="ShaderNodeUVMap")
            uvmap =  bpy.context.active_node
            bpy.context.active_node.location[0] = noisenode.location[0]-200
            bpy.context.active_node.location[1] = noisenode.location[1]
            links.new(bpy.context.active_node.outputs[0], noisenode.inputs[0])
            
            bpy.ops.node.add_node(type="ShaderNodeEmission")
            emission =  bpy.context.active_node
            bpy.context.active_node.location[0] = noisenode.location[0]+200
            bpy.context.active_node.location[1] = noisenode.location[1]
            links.new(noisenode.outputs[0], bpy.context.active_node.inputs[0])
            links.new(bpy.context.active_node.outputs[0], output.inputs[0])
            
            bpy.ops.node.add_node(type="ShaderNodeTexImage")
            image = bpy.context.active_node
            bpy.context.active_node.location[0] = noisenode.location[0]-300
            bpy.context.active_node.location[1] = noisenode.location[1]
            bpy.context.active_node.image = noisebake
            
            bpy.ops.object.bake(type='EMIT')
            noisebake.pack()
            noisebake.filepath = context.scene.transmatpaths.exportdirectory + str(noisebake.name).replace(' ','').replace('.','') + ".png"
            noisebake.file_format = "PNG"
            noisebake.save()
            nodes.remove(uvmap)
            nodes.remove(emission)
            links.new(image.outputs[0],nnlinksocket) 
               
        bpy.context.scene.render.engine = previousrenderengine
            
        return {'FINISHED'}      
                
################################################################################
# Operator Code
################################################################################

class TransMatOperator(bpy.types.Operator):
    """Translates and Transfers Materials from Blender to Unreal"""
    bl_idname = "blui.transmat_operator"
    bl_label = "Transfer Material!"

    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.type == 'NODE_EDITOR'

    def execute(self, context):
        
        material = bpy.context.material
        
        supported_nodes = [
        "ShaderNodeFresnel",
        "ShaderNodeUVMap",
        "ShaderNodeSeparateRGB",
        "NodeReroute",
        "ShaderNodeOutputMaterial",
        "ShaderNodeBsdfPrincipled",
        "ShaderNodeMixShader",
        "ShaderNodeAddShader",
        "ShaderNodeInvert",
        "ShaderNodeTexImage",
        "ShaderNodeTexCoord",
        "ShaderNodeValue",
        "ShaderNodeRGB",
        "ShaderNodeMath",
        "ShaderNodeVectorMath",
        "ShaderNodeMixRGB"
        ]
        
        # Thanks to Jim Kroovy for this - prevents crashes with unsupported nodes
        nodes = [n for n in material.node_tree.nodes if n.bl_idname in supported_nodes]
        
        node_translate = {
        "ShaderNodeFresnel":"unreal.MaterialExpressionFresnel",
        "ShaderNodeUVMap":"unreal.MaterialExpressionTextureCoordinate",
        "ShaderNodeSeparateRGB":"unreal.MaterialExpressionMaterialFunctionCall",
        "NodeReroute":"unreal.MaterialExpressionReroute",
        "ShaderNodeOutputMaterial":"",
        "ShaderNodeBsdfPrincipled":"unreal.MaterialExpressionMakeMaterialAttributes",
        "ShaderNodeMixShader":"unreal.MaterialExpressionBlendMaterialAttributes",
        "ShaderNodeAddShader":"unreal.MaterialExpressionAdd",
        "ShaderNodeInvert":"unreal.MaterialExpressionOneMinus",
        "ShaderNodeTexImage":"unreal.MaterialExpressionTextureSample",
        "ShaderNodeTexCoord":"unreal.MaterialExpressionTextureCoordinate",
        "ShaderNodeValue":"unreal.MaterialExpressionConstant",
        "ShaderNodeRGB":"unreal.MaterialExpressionConstant3Vector",
        # Math Node Operations
        "ADD":"unreal.MaterialExpressionAdd",
        "SUBTRACT":"unreal.MaterialExpressionSubtract",
        "MULTIPLY":"unreal.MaterialExpressionMultiply",
        "DIVIDE":"unreal.MaterialExpressionDivide",
        "SINE":"unreal.MaterialExpressionSine",
        "ARCSINE":"unreal.MaterialExpressionArcsine",
        "COSINE":"unreal.MaterialExpressionCosine",
        "ARCCOSINE":"unreal.MaterialExpressionArccossine",
        "POWER":"unreal.MaterialExpressionPower",
        "MINIMUM":"unreal.MaterialExpressionMin",
        "MAXIMUM":"unreal.MaterialExpressionMax",
        "ROUND":"unreal.MaterialExpressionRound",
        "ABSOLUTE":"unreal.MaterialExpressionAbs",
        # Vector Math Node Operations
        "NORMALIZE":"unreal.MaterialExpressionNormalize",
        "DOT_PRODUCT":"unreal.MaterialExpressionDotProduct",
        "CROSS_PRODUCT":"unreal.MaterialExpressionCrossProduct",
        # Mix RGB Blend Types
        "MIX":"unreal.MaterialExpressionLinearInterpolate",
        "BURN":"unreal.MaterialExpressionMaterialFunctionCall",
        "DODGE":"unreal.MaterialExpressionMaterialFunctionCall",
        "DARKEN":"unreal.MaterialExpressionMaterialFunctionCall",
        "DIFFERENCE":"unreal.MaterialExpressionMaterialFunctionCall",
        "LIGHTEN":"unreal.MaterialExpressionMaterialFunctionCall",
        "LINEAR_LIGHT":"unreal.MaterialExpressionMaterialFunctionCall",
        "OVERLAY":"unreal.MaterialExpressionMaterialFunctionCall",
        "SCREEN":"unreal.MaterialExpressionMaterialFunctionCall",
        "SOFT_LIGHT":"unreal.MaterialExpressionMaterialFunctionCall",
        }
        
        inputsockets = []
        
        uenodes = []

################################################################################        
# Setting up the Unreal script
################################################################################
        
        # Exporting the material as a .py file to be run in Unreal
        with open(f'{context.scene.transmatpaths.exportdirectory}{material.name}_TM.py', 'w') as textoutput:
            # The file will contain all the print statements until execute
            # returns 'FINISHED'
            with redirect_stdout(textoutput):
                        
                print("import unreal")
                print("")
                print(f"{material.name}=unreal.AssetToolsHelpers.get_asset_tools().create_asset('{material.name}','/Game/{context.scene.transmatpaths.materialdirectory}', unreal.Material, unreal.MaterialFactoryNew())")
                print(f"{material.name}.set_editor_property('use_material_attributes',True)")
                print("")
                print("create_expression = unreal.MaterialEditingLibrary.create_material_expression")
                print("create_connection = unreal.MaterialEditingLibrary.connect_material_expressions")
                print("connect_property = unreal.MaterialEditingLibrary.connect_material_property")
                print(f"tasks = []")
                
##########################################################################`######
# Importing the textures
################################################################################
                
                print("")
                print("### Textures")
                for node in nodes:
                    if node.bl_idname == "ShaderNodeTexImage":
                        filename = str(node.image.filepath).replace('/','').replace('.','_').replace(' ','').replace(':','').replace('\\','')
                        print("")
                        print(f"{filename} = '{str(node.image.filepath_from_user())}'")
                        print("")
                        print(f"{filename}_import = unreal.AssetImportTask()")
                        print(f"{filename}_import.set_editor_property('automated',True)")
                        print(f"{filename}_import.set_editor_property('destination_path','/Game/{context.scene.transmatpaths.texturedirectory}')")
                        print(f"{filename}_import.set_editor_property('destination_name','{filename}')")
                        print(f"{filename}_import.set_editor_property('factory',unreal.TextureFactory())")
                        print(f"{filename}_import.set_editor_property('filename',{filename})")                
                        print(f"{filename}_import.set_editor_property('replace_existing',True)")
                        print(f"{filename}_import.set_editor_property('save',True)")
                        print(f"tasks.append({filename}_import)")
                print("")
                print(f"unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)")
                
################################################################################
# Creating the Nodes
################################################################################

                print("")
                print("### Nodes")
                for node in nodes:

                    nodeinfo = {
                    "Blender Node": node.bl_idname,
                    "Unreal_Node": "",
                    "Node ID": node.name,
                    "Settings": {}
                    }
                    
                    uenodename = node.name.replace(".","").replace(" ","")
                    node.name = uenodename
                                            
                    # Math node retrieves the operation: ADD, MULTIPLY, COSINE, etc
                    if node.bl_idname == "ShaderNodeMath":
                        nodeinfo["Unreal_Node"] = node_translate[node.operation]
                        
                    # Math node retrieves the operation: NORMALIZE, CROSS_PRODUCT etc
                    if node.bl_idname == "ShaderNodeVectorMath":
                        nodeinfo["Unreal_Node"] = node_translate[node.operation]
                            
                    # Mix RGB Node retrieves the Blend Type
                    if node.bl_idname == "ShaderNodeMixRGB":
                        nodeinfo["Unreal_Node"] = node_translate[node.blend_type]                    
                    
                    # For all other node types, use the bl.id_name
                    if not node.bl_idname == "ShaderNodeMixRGB" and not node.bl_idname == "ShaderNodeMath" and not node.bl_idname == "ShaderNodeVectorMath":
                        nodeinfo["Unreal_Node"] = node_translate[node.bl_idname]                          
                    
                    if not node.bl_idname == 'ShaderNodeOutputMaterial':    
                        print(f"{str(uenodename)} = create_expression({material.name},{nodeinfo['Unreal_Node']},{node.location[0]-800},{node.location[1]-400})")    
                        uenodes.append(node)

################################################################################
# Loading Material Functions and Image Textures
################################################################################                
                                
                print("")
                print("### Material Functions")        
                for node in uenodes:
                    if node.bl_idname == "ShaderNodeMixRGB" and node.blend_type == 'BURN':
                        print(f"mat_func_burn = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_ColorBurn')")
                        print(f"{node.name}.set_editor_property('material_function',mat_func_burn)")
                    if node.bl_idname == "ShaderNodeMixRGB" and node.blend_type == 'DODGE':
                        print(f"mat_func_dodge = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_ColorDodge')")
                        print(f"{node.name}.set_editor_property('material_function',mat_func_dodge)")
                    if node.bl_idname == "ShaderNodeMixRGB" and node.blend_type == 'DARKEN':
                        print(f"mat_func_darken = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_Darken')")
                        print(f"{node.name}.set_editor_property('material_function',mat_func_darken)")
                    if node.bl_idname == "ShaderNodeMixRGB" and node.blend_type == 'DIFFERENCE':
                        print(f"mat_func_difference = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_Difference')")
                        print(f"{node.name}.set_editor_property('material_function',mat_func_difference)")
                    if node.bl_idname == "ShaderNodeMixRGB" and node.blend_type == 'LIGHTEN':
                        print(f"mat_func_lighten = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_Lighten')")
                        print(f"{node.name}.set_editor_property('material_function',mat_func_lighten)")
                    if node.bl_idname == "ShaderNodeMixRGB" and node.blend_type == 'LINEAR_LIGHT':
                        print(f"mat_func_linear_light = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_LinearLight')")
                        print(f"{node.name}.set_editor_property('material_function',mat_func_linear_light)")
                    if node.bl_idname == "ShaderNodeMixRGB" and node.blend_type == 'OVERLAY':
                        print(f"mat_func_overlay = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_Overlay')")
                        print(f"{node.name}.set_editor_property('material_function',mat_func_overlay)")
                    if node.bl_idname == "ShaderNodeMixRGB" and node.blend_type == 'SCREEN':
                        print(f"mat_func_screen = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_Screen')")
                        print(f"{node.name}.set_editor_property('material_function',mat_func_screen)")
                    if node.bl_idname == "ShaderNodeMixRGB" and node.blend_type == 'SOFT_LIGHT':
                        print(f"mat_func_soft_light = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_SoftLight')")
                        print(f"{node.name}.set_editor_property('material_function',mat_func_soft_light)")
                        
                    if node.bl_idname == "ShaderNodeSeparateRGB":
                        print(f"mat_func_separate = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions02/Utility/BreakOutFloat3Components')")
                        print(f"{node.name}.set_editor_property('material_function',mat_func_separate)")
                    
                    # Troublesome slash is here
                    if node.bl_idname == "ShaderNodeTexImage":
                        filename = str(node.image.filepath).replace('/','').replace('.','_').replace(' ','').replace(':','').replace('\\','')
                        print(f"{node.name}.texture = unreal.load_asset('/Game{context.scene.transmatpaths.texturedirectory}/{filename}')")


################################################################################
# Making the connections
################################################################################                
                                
                print("")
                print("### Connections")        
                for node in uenodes:
                    for input in node.inputs:
                            if node.bl_idname == "ShaderNodeMath":
                                if not node.inputs[0].is_linked:
                                    print(f"{node.name}.const_a = {node.inputs[0].default_value}")
                                if not node.inputs[1].is_linked:    
                                    print(f"{node.name}.const_b = {node.inputs[1].default_value}")
                                    
                    #looping through the outputs
                    for output in node.outputs:
                        # only checking those that are connected
                        if output.is_linked:
                            for link in output.links:                               
                                if node.bl_idname == "ShaderNodeRGB":
                                    print(f"{node.name}.constant = ({node.outputs[0].default_value[0]},{node.outputs[0].default_value[1]},{node.outputs[0].default_value[2]})")
                                                            
                                if node.bl_idname == 'ShaderNodeValue':
                                    print(f"{node.name}.r = {node.outputs[0].default_value}")
                                    inputsockets = [
                                    "A",
                                    "B"
                                    ]
                                                                                                        
                                if link.to_node.bl_idname == "ShaderNodeMath":
                                    inputsockets = [
                                    "A",
                                    "B"
                                    ]
                                
                                if link.to_node.bl_idname == "ShaderNodeVectorMath" and link.to_node.operation == "NORMALIZE":
                                    inputsockets = [
                                    "VectorInput",
                                    ""
                                    ]
                                    
                                if link.to_node.bl_idname == "ShaderNodeSeparateRGB":
                                    inputsockets = [
                                    "Float3",
                                    ""
                                    ]
                                   
                                if link.to_node.bl_idname == "ShaderNodeBsdfPrincipled":
                                    inputsockets = [
                                    "BaseColor",#0
                                    "Subsurface",#1
                                    "SubsurfaceRadius",#2
                                    "SubsurfaceColor",#3
                                    "Metallic",#4
                                    "Specular",#5
                                    "SpecularTint",#6
                                    "Roughness",#7
                                    "Anisotropy",#8
                                    "AnisotropicRotation",#9
                                    "Sheen",#10
                                    "SheenTint",#11
                                    "ClearCoat",#12
                                    "ClearCoatRoughness",#13
                                    "Refraction",#14
                                    "Transmission",#15
                                    "TransmissionRoughness",#16
                                    "EmissiveColor",#17
                                    "Opacity",#18
                                    "Normal",#19
                                    "ClearCoatNormal",#20
                                    "Tangent"#21
                                    ]
                                    
                                if link.to_node.bl_idname == "ShaderNodeMixRGB" and link.to_node.blend_type == "MIX":
                                    inputsockets = [
                                    "A",
                                    "B",
                                    "Alpha",
                                    ]
                                
                                if link.to_node.bl_idname == "ShaderNodeMixRGB" and not link.to_node.blend_type == "MIX":
                                    inputsockets = [
                                    "Blend",
                                    "Base"
                                    ]    
                                    
                                if link.to_node.bl_idname == "ShaderNodeTexImage":
                                    inputsockets = [
                                    "UVs",
                                    "Tex"
                                    ]
                                    
                                if link.to_node.bl_idname == "ShaderNodeInvert":
                                    inputsockets = [
                                    "",
                                    ""
                                    ]
                                
                                if link.to_node.bl_idname == "NodeReroute":
                                    inputsockets = [
                                    "",
                                    ""
                                    ]
                                    
                                if link.to_node.bl_idname == "ShaderNodeAddShader":
                                    inputsockets = [
                                    "A",
                                    "B"
                                    ]
                                    
                                if link.to_node.bl_idname == "ShaderNodeMixShader":
                                    inputsockets = [
                                    "A",
                                    "B"
                                    ]
                                    
                                if link.to_node.bl_idname == "ShaderNodeOutputMaterial":
                                    print("# Output Node")
                                    #print(f"{node.name}_connection = connect_property({link.from_node.name},'','Material Attributes')")
                                
                                if not link.to_node.bl_idname == "ShaderNodeOutputMaterial":    
                                    socketindex = link.to_socket.path_from_id()
                                    socketindex_formatted = re.search(r"\[([A-Za-z0-9_]+)\]", socketindex)    
                                    print(f"{node.name}_connection = create_connection({link.from_node.name},'',{link.to_node.name},'{inputsockets[int(socketindex_formatted.group(1))]}')")

################################################################################
                                                
        return {'FINISHED'}

################################################################################
# Panel UI
################################################################################

class TransMatPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the node editor"""
    bl_label = "TransMat"
    bl_idname = "BLUI_PT_transmat"
    bl_category = "TransMat"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout
        
        column = layout.column()
        column.label(text="Export Directory", icon='FILE_FOLDER')
        column.label(text="(Folder where the .py will be saved)")
        
        row = layout.row()
        row.prop(context.scene.transmatpaths, 'exportdirectory')
        
        column = layout.column()
        column.label(text="")
        
        column = layout.column()
        column.label(text="Unreal Import Subfolders", icon='FILE_FOLDER')
        column.label(text="(relative to Game/Content/)")
        
        row = layout.row()
        row.prop(context.scene.transmatpaths, 'materialdirectory')
        
        row = layout.row()
        row.prop(context.scene.transmatpaths, 'texturedirectory')
        
        column = layout.column()
        column.label(text="")
        
        column = layout.column()
        column.label(text="Bake noise nodes to textures", icon='NODE_SEL')
        column.label(text="(Textures save to Export folder)")
        
        row = layout.row()
        row.prop(context.scene.transmatpaths, 'noiseresolution')
        
        row = layout.row()
        row.operator("blui.bakenoises_operator", icon='NODE')
        
        column = layout.column()
        column.label(text="")
        
        column = layout.column()
        column.label(text="Translate Material for Unreal", icon='MATERIAL')
        
        row = layout.row()
        row.operator("blui.transmat_operator", icon='EXPORT')

# Register

def register():
    bpy.utils.register_class(TransMatPanel)
    bpy.utils.register_class(TransMatOperator)
    bpy.utils.register_class(TransmatPaths)
    bpy.types.Scene.transmatpaths = bpy.props.PointerProperty(type=TransmatPaths)
    bpy.utils.register_class(BakeNoises)

def unregister():
    bpy.utils.unregister_class(TransMatPanel)
    bpy.utils.unregister_class(TransMatOperator)
    bpy.utils.unregister_class(TransmatPaths)
    del bpy.types.Scene.transmatpaths
    bpy.utils.unregister_class(BakeNoises)
    
if __name__ == "__main__":
    register()
