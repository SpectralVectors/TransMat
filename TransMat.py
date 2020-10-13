import bpy
import re
from contextlib import redirect_stdout

# Operator Code

class TransMatOperator(bpy.types.Operator):
    """Translates and Transfers Materials from Blender to Unreal"""
    bl_idname = "blui.transmat_operator"
    bl_label = "TransMat!"

    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.type == 'NODE_EDITOR'

    def execute(self, context):
        
        material = bpy.context.material
        nodes = material.node_tree.nodes
        gamecontentdirectory = "/Game/"
        exportdirectory = "D:\Blender\Scripts\TransmatOutputs\_"
        
        node_translate = {
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
        # Mix RGB Blend Types
        "MIX":"unreal.MaterialExpressionLinearInterpolate"
        }
        
        inputsockets = []
        
        uenodes = []

################################################################################        
# Setting up the Unreal script
################################################################################
        
        # Exporting the material as a .py file to be run in Unreal
        with open(f'{exportdirectory}{material.name}_TM.py', 'w') as textoutput:
            # The file will contain all the print statements until execute
            # returns 'FINISHED'
            with redirect_stdout(textoutput):
                        
                print("import unreal")
                print("")
                print(f"{material.name}=unreal.AssetToolsHelpers.get_asset_tools().create_asset('{material.name}','{gamecontentdirectory}', unreal.Material, unreal.MaterialFactoryNew())")
                print(f"{material.name}.set_editor_property('use_material_attributes',True)")
                print("")
                print("create_expression = unreal.MaterialEditingLibrary.create_material_expression")
                print("create_connection = unreal.MaterialEditingLibrary.connect_material_expressions")
                print("connect_property = unreal.MaterialEditingLibrary.connect_material_property")
                print(f"tasks = []")
                #print(f"results = []")
                
################################################################################
# Importing the textures
################################################################################
                
                print("")
                print("### Textures")
                for node in nodes:
                    if node.bl_idname == "ShaderNodeTexImage":
                        print("")
                        print(f"{str(node.image.filepath).replace('/','').replace('.','_')} = '{str(node.image.filepath_from_user())}'")
                        print("")
                        print(f"{str(node.image.filepath).replace('/','').replace('.','_')}_import = unreal.AssetImportTask()")
                        print(f"{str(node.image.filepath).replace('/','').replace('.','_')}_import.set_editor_property('automated',True)")
                        print(f"{str(node.image.filepath).replace('/','').replace('.','_')}_import.set_editor_property('destination_path','{gamecontentdirectory}')")
                        print(f"{str(node.image.filepath).replace('/','').replace('.','_')}_import.set_editor_property('destination_name','{str(node.image.filepath).replace('/','').replace('.','_')}')")
                        print(f"{str(node.image.filepath).replace('/','').replace('.','_')}_import.set_editor_property('factory',unreal.TextureFactory())")
                        print(f"{str(node.image.filepath).replace('/','').replace('.','_')}_import.set_editor_property('filename',{str(node.image.filepath).replace('/','').replace('.','_')})")                
                        print(f"{str(node.image.filepath).replace('/','').replace('.','_')}_import.set_editor_property('replace_existing',True)")
                        print(f"{str(node.image.filepath).replace('/','').replace('.','_')}_import.set_editor_property('save',True)")
                        print(f"tasks.append({str(node.image.filepath).replace('/','').replace('.','_')}_import)")
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
                    
                    # Value node contains a single float
                    if node.bl_idname == 'ShaderNodeValue':
                        nodeinfo["Unreal_Node"] = node_translate[node.bl_idname]
                        
                    # RGB node gives 4 float values for RGBA - alpha may be unnecessary
                    if node.bl_idname == "ShaderNodeRGB":
                        nodeinfo["Unreal_Node"] = node_translate[node.bl_idname]
                        
                    # Math node retrieves the operation: ADD, MULTIPLY, COSINE, etc
                    if node.bl_idname == "ShaderNodeMath":
                        nodeinfo["Unreal_Node"] = node_translate[node.operation]
                        
                    # Principled BSDF looks at inputs, rather than outputs
                    if node.bl_idname == "ShaderNodeBsdfPrincipled":
                        nodeinfo["Unreal_Node"] = node_translate[node.bl_idname]
                        
                    # Mix RGB Node retrieves the Blend Type
                    if node.bl_idname == "ShaderNodeMixRGB":
                        nodeinfo["Unreal_Node"] = node_translate[node.blend_type]
                        
                    # Texture Coordinate
                    if node.bl_idname =="ShaderNodeTexCoord":
                        nodeinfo["Unreal_Node"] = node_translate[node.bl_idname]
                        
                    # Image Texture Node    
                    if node.bl_idname == "ShaderNodeTexImage":
                        nodeinfo["Unreal_Node"] = node_translate[node.bl_idname]
                        
                    # Invert Node    
                    if node.bl_idname == "ShaderNodeInvert":
                        nodeinfo["Unreal_Node"] = node_translate[node.bl_idname]
                        
                    # Add Shader Node    
                    if node.bl_idname == "ShaderNodeAddShader":
                        nodeinfo["Unreal_Node"] = node_translate[node.bl_idname]
                        
                    # Mix Shader Node    
                    if node.bl_idname == "ShaderNodeMixShader":
                        nodeinfo["Unreal_Node"] = node_translate[node.bl_idname]      
                    
                    if not node.bl_idname == 'ShaderNodeOutputMaterial':    
                        print(f"{str(uenodename)} = create_expression({material.name},{nodeinfo['Unreal_Node']},{node.location[0]-800},{node.location[1]-400})")    
                        uenodes.append(node)

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
                                    
                                if link.to_node.bl_idname == "ShaderNodeMixRGB":
                                    inputsockets = [
                                    "A",
                                    "B"
                                    ]
                                    
                                if link.to_node.bl_idname == "ShaderNodeTexImage":
                                    inputsockets = [
                                    "UVs",
                                    "B"
                                    ]
                                    
                                if link.to_node.bl_idname == "ShaderNodeInvert":
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
                                    print("")
                                    #print(f"{node.name}_connection = connect_property({link.from_node.name},'','Material Attributes')")
                                
                                if not link.to_node.bl_idname == "ShaderNodeOutputMaterial":    
                                    socketindex = link.to_socket.path_from_id()
                                    socketindex_formatted = re.search(r"\[([A-Za-z0-9_]+)\]", socketindex)    
                                    print(f"{node.name}_connection = create_connection({link.from_node.name},'',{link.to_node.name},'{inputsockets[int(socketindex_formatted.group(1))]}')")
                   
################################################################################
# Inputting the values & Images into Nodes
################################################################################
                                
                print("")
                print("### Settings")        
                for node in uenodes:
                        
                    if node.bl_idname == "ShaderNodeMixRGB":
                        if not node.inputs[1].is_linked:
                            print(f"{node.name}.const_a = ({node.inputs[1].default_value[0]},{node.inputs[1].default_value[1]},{node.inputs[1].default_value[2]})")
                        if not node.inputs[2].is_linked:    
                            print(f"{node.name}.const_b = ({node.inputs[2].default_value[0]},{node.inputs[2].default_value[1]},{node.inputs[2].default_value[2]})")
                        if not node.inputs[0].is_linked:
                            print(f"{node.name}.const_alpha = {node.inputs[0].default_value}")
                    
#                    if node.bl_idname == "ShaderNodeMixShader":
#                        if not node.inputs[0].is_linked:
#                            print(f"{node.name}.const_alpha = {node.inputs[0].default_value}")

                    if node.bl_idname == "ShaderNodeTexImage":
                        print(f"{node.name}.texture = unreal.load_asset('{gamecontentdirectory}{str(node.image.filepath).replace('/','').replace('.','_')}')")
                                                                                   
################################################################################

                                                
        return {'FINISHED'}


# Panel UI

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
        layout.label(text="Transfer Material!->", icon='MATERIAL')

        row = layout.row()
        row.operator("blui.transmat_operator")

# Register

def register():
    bpy.utils.register_class(TransMatPanel)
    bpy.utils.register_class(TransMatOperator)

def unregister():
    bpy.utils.unregister_class(TransMatPanel)
    bpy.utils.unregister_class(TransMatOperator)

if __name__ == "__main__":
    register()
