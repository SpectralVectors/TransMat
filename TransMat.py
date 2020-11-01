import bpy
import re
from contextlib import redirect_stdout

bl_info = {
    'name': 'TransMat',
    'category': 'Node Editor',
    'author': 'Spectral Vectors',
    'version': (0, 3, 3),
    'blender': (2, 90, 0),
    'location': 'Node Editor',
    "description": "Automatically recreates Blender materials in Unreal"
}

################################################################################
# Properties & Directory Code
################################################################################

class TransmatPaths(bpy.types.PropertyGroup):
    
    exportdirectory : bpy.props.StringProperty(
        name = "Export",
        description = "Folder where the .py will be saved",
        default = "",
        subtype = 'DIR_PATH'
    )
    
    materialdirectory : bpy.props.StringProperty(
        name= "Material",
        description="Subfolder to save Materials to, relative to Game/Content/",
        default = "Materials"
    )
    
    texturedirectory : bpy.props.StringProperty(
        name= "Texture",
        description="Subfolder to save Textures to, relative to Game/Content/",
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
    """Bakes procedural noise nodes to textures for export, textures are saved in the Export folder"""
    bl_idname = "blui.bakenoises_operator"
    bl_label = "Bake Noise Nodes"
    
    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.type == 'NODE_EDITOR'

    def execute(self, context):
        
        # Save the current render engine to reset after baking
        previousrenderengine = bpy.context.scene.render.engine
        material = bpy.context.material
        nodes = material.node_tree.nodes
        links = material.node_tree.links
        noisenodes = []
        rebuildnodegroups = {}
        
################################################################################        
        # Breaking the Groups, a better solution can be found for reassembling later
        for node in nodes:
            if node.bl_idname == "ShaderNodeGroup":
#                groupednodes = []
#                groupednodes.append(node.node_tree.nodes)
#                rebuildnodegroups.append(groupednodes)
                material.node_tree.nodes.active = node
                bpy.ops.node.group_ungroup()
################################################################################
        
        # Set the render engine to Cycles
        bpy.context.scene.render.engine = 'CYCLES'
        bpy.context.scene.cycles.device = 'GPU'
        bpy.context.scene.cycles.samples = 128
        
        # Loop through all the nodes, all procedural texture nodes start with
        # "ShaderNodeTex...", once we remove the Image Texture node, all that
        # remains are the procedurals, and we make a list of just those
        for node in nodes:
            if node.bl_idname.startswith("ShaderNodeTex") and not node.bl_idname == "ShaderNodeTexImage":
                noisenode = node
                noisenodes.append(noisenode)
            # Making note of the Output node, so that we can connect the Emission
            # shader for baking
            if node.bl_idname == "ShaderNodeOutputMaterial":
                output = node
        
        # In our noise node list, we make a note of the output connection, so that
        # we can reconnect the baked textures to the procedural textures outputs        
        for noisenode in noisenodes:
            for link in noisenode.outputs[0].links:
                nnlinksocket = link.to_socket
            
            # Make a new image that is the width and height the user specifies in
            # the Addon's panel            
            noisebake = bpy.data.images.new(
            name = str(noisenode.name).replace('.','_').replace(' ',''), 
            width = context.scene.transmatpaths.noiseresolution, 
            height = context.scene.transmatpaths.noiseresolution
            )
            
            # Create a UV Map node, store a reference to it, move it to the left
            # of the node we'll be baking from, then link it to the noise node
            bpy.ops.node.add_node(type="ShaderNodeUVMap")
            uvmap =  bpy.context.active_node
            bpy.context.active_node.location[0] = noisenode.location[0]-200
            bpy.context.active_node.location[1] = noisenode.location[1]
            links.new(bpy.context.active_node.outputs[0], noisenode.inputs[0])
            
            # Create an Emission Shader, store a reference to it, move it to the right
            # of the node we'll be baking from, then link it to the noise node 
            bpy.ops.node.add_node(type="ShaderNodeEmission")
            emission =  bpy.context.active_node
            bpy.context.active_node.location[0] = noisenode.location[0]+200
            bpy.context.active_node.location[1] = noisenode.location[1]
            links.new(noisenode.outputs[0], bpy.context.active_node.inputs[0])
            links.new(bpy.context.active_node.outputs[0], output.inputs[0])
            
            # Create an Image Texture node, store a reference to it, move it to the left
            # of the noise node, then assign the texture we created to the node
            # It's important that this is the last node created, because Blender
            # looks for the active node, with a loaded texture as a bake target
            bpy.ops.node.add_node(type="ShaderNodeTexImage")
            image = bpy.context.active_node
            bpy.context.active_node.location[0] = noisenode.location[0]-250
            bpy.context.active_node.location[1] = noisenode.location[1]
            bpy.context.active_node.image = noisebake
            
            # Now we tell it to bake the Emission pass, pack the image into the .blend
            # save it to the Export directory as a PNG, then remove the UV Map
            # and Emission Shader, before connecting the newly baked texture node
            # to the same output connection the noise node was connected to
            bpy.ops.object.bake(type='EMIT')
            noisebake.pack()
            noisebake.filepath = context.scene.transmatpaths.exportdirectory + str(noisebake.name).replace(' ','').replace('.','') + ".png"
            noisebake.file_format = "PNG"
            noisebake.save()
            nodes.remove(uvmap)
            nodes.remove(emission)
            links.new(image.outputs[0],nnlinksocket) 
        
        # Reset the render engine to the user's previous setting       
        bpy.context.scene.render.engine = previousrenderengine
           
#        for groupnodes in rebuildnodegroups:
#            for node in groupnodes:
                
        
        return {'FINISHED'}      
                
################################################################################
# Operator Code
################################################################################

class TransMatOperator(bpy.types.Operator):
    """Translates and Transfers Materials from Blender to Unreal"""
    bl_idname = "blui.transmat_operator"
    bl_label = "Transfer Material!"
    
    # Make sure we're in the Node Editor
    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.type == 'NODE_EDITOR'
        
    def execute(self, context):
        
        # The officially supported Node List (in .bl_idname form)
        supported_nodes = [
        "ShaderNodeFresnel",
        "ShaderNodeUVMap",
        "ShaderNodeSeparateRGB",
        "ShaderNodeSeparateXYZ",
        "ShaderNodeSeparateHSV",
        "ShaderNodeCombineRGB",
        "ShaderNodeCombineXYZ",
        "ShaderNodeCombineHSV",
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
        
        # A dictionary with all our nodes paired with their Unreal counterparts 
        node_translate = {
        "ShaderNodeFresnel":"unreal.MaterialExpressionFresnel",
        "ShaderNodeUVMap":"unreal.MaterialExpressionTextureCoordinate",
        "ShaderNodeSeparateRGB":"unreal.MaterialExpressionMaterialFunctionCall",
        "ShaderNodeSeparateXYZ":"unreal.MaterialExpressionMaterialFunctionCall",
        "ShaderNodeSeparateHSV":"unreal.MaterialExpressionMaterialFunctionCall",
        "ShaderNodeCombineRGB":"unreal.MaterialExpressionMaterialFunctionCall",
        "ShaderNodeCombineXYZ":"unreal.MaterialExpressionMaterialFunctionCall",
        "ShaderNodeCombineHSV":"unreal.MaterialExpressionMaterialFunctionCall",
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
        
        # A dictionary with all our nodes and their Blender sockets, paired with their Unreal socket counterparts
        # Some are left blank, as Unreal will grab the default output if you supply no name
        socket_translate = {
        # Principled BSDF
        "ShaderNodeBsdfPrincipled": {
        "Base Color":"BaseColor",#0
        "Subsurface":"Subsurface",#1
        "Subsurface Radius":"SubsurfaceRadius",#2
        "Subsurface Color":"SubsurfaceColor",#3
        "Metallic":"Metallic",#4
        "Specular":"Specular",#5
        "Specular Tint":"SpecularTint",#6
        "Roughness":"Roughness",#7
        "Anisotropic":"Anisotropy",#8
        "Anisotropic Rotation":"AnisotropicRotation",#9
        "Sheen":"Sheen",#10
        "Sheen Tint":"SheenTint",#11
        "Clearcoat":"ClearCoat",#12
        "Clearcoat Roughness":"ClearCoatRoughness",#13
        "IOR":"Refraction",#14
        "Transmission":"Transmission",#15
        "Transmission Roughness":"TransmissionRoughness",#16
        "Emission":"EmissiveColor",#17
        "Alpha":"Opacity",#18
        "Normal":"Normal",#19
        "Clearcoat Normal":"ClearCoatNormal",#20
        "Tangent":"Tangent",#21
        "BSDF":"",},
        "ShaderNodeValue": {"Value":"R"},
        "ShaderNodeRGB": {"Color":"Constant"},
        "ShaderNodeSeparateRGB":{"Image":"Float3","R":"R","G":"G","B":"B"},
        "ShaderNodeSeparateXYZ":{"Vector":"Float3","X":"R","Y":"G","Z":"B"},
        "ShaderNodeSeparateHSV":{"Image":"Float3","H":"R","S":"G","V":"B"},
        "ShaderNodeCombineRGB":{"Image":"Result","R":"X","G":"Y","B":"Z"},
        "ShaderNodeCombineXYZ":{"Vector":"Result","X":"X","Y":"Y","Z":"Z"},
        "ShaderNodeCombineHSV":{"Image":"Result","H":"X","S":"Y","V":"Z"},
        "ShaderNodeTexImage":{"Vector":"UVs","Color":"RGB"},
        "ShaderNodeFresnel":{"Fac":""},
        "ShaderNodeUVMap":{"UV":""},
        "NodeReroute":{"":""},
        "ShaderNodeMixShader":{"0":"Alpha","1":"A","2":"B","Shader":""},
        "ShaderNodeAddShader":{"0":"A","1":"B", "Shader":""},
        "ShaderNodeInvert":{"":""},
        "ShaderNodeTexCoord":{"":""},
        # Math Node Operations
        "ADD":{"0":"A","1":"B", "Scale":"","Value":""},
        "SUBTRACT":{"0":"A","1":"B","Value":""},
        "MULTIPLY":{"0":"A","1":"B","Value":""},
        "DIVIDE":{"0":"A","1":"B","Value":""},
        "SINE":{"0":"","Value":""},
        "ARCSINE":{"0":"","Value":""},
        "COSINE":{"0":"","Value":""},
        "ARCCOSINE":{"0":"","Value":""},
        "POWER":{"0":"A","1":"B","Value":""},
        "MINIMUM":{"0":"A","1":"B","Value":""},
        "MAXIMUM":{"0":"A","1":"B","Value":""},
        "ROUND":{"0":"","Value":""},
        "ABSOLUTE":{"0":"","Value":""},
        # Vector Math Node Operations
        "NORMALIZE":{"0":"A","1":"B","Vector":""},
        "DOT_PRODUCT":{"0":"A","1":"B","Vector":""},
        "CROSS_PRODUCT":{"0":"A","1":"B","Vector":""},
        # Mix RGB Blend Types
        "MIX":{"Color1":"A", "Color2":"B", "Fac":"Alpha", "Color":""},
        "BURN":{"Color1":"Base", "Color2":"Blend", "Fac":"Alpha", "Color":""},
        "DODGE":{"Color1":"Base", "Color2":"Blend", "Fac":"Alpha", "Color":""},
        "DARKEN":{"Color1":"Base", "Color2":"Blend", "Fac":"Alpha", "Color":""},
        "DIFFERENCE":{"Color1":"Base", "Color2":"Blend", "Fac":"Alpha", "Color":""},
        "LIGHTEN":{"Color1":"Base", "Color2":"Blend", "Fac":"Alpha", "Color":""},
        "LINEAR_LIGHT":{"Color1":"Base", "Color2":"Blend", "Fac":"Alpha", "Color":""},
        "OVERLAY":{"Color1":"Base", "Color2":"Blend", "Fac":"Alpha", "Color":""},
        "SCREEN":{"Color1":"Base", "Color2":"Blend", "Fac":"Alpha", "Color":""},
        "SOFT_LIGHT":{"Color1":"Base", "Color2":"Blend", "Fac":"Alpha", "Color":""},
        }
        
        # A dictionary with our Blender nodes and their Unreal MaterialFunction counterparts
        material_function = {
        'BURN':'mat_func_burn',
        'DODGE':'mat_func_dodge',
        'DARKEN':'mat_func_darken',
        'DIFFERENCE':'mat_func_difference',
        'LIGHTEN':'mat_func_lighten',
        'LINEAR_LIGHT':'mat_func_linear_light',
        'OVERLAY':'mat_func_overlay',
        'SCREEN':'mat_func_screen',
        'SOFT_LIGHT':'mat_func_soft_light',
        "ShaderNodeSeparateRGB":'mat_func_separate',
        "ShaderNodeSeparateXYZ":'mat_func_separate',
        "ShaderNodeSeparateHSV":'mat_func_separate',
        "ShaderNodeCombineRGB":'mat_func_combine',
        "ShaderNodeCombineXYZ":'mat_func_combine',
        "ShaderNodeCombineHSV":'mat_func_combine',
        }
        
        # Acting on the currently active material
        material = bpy.context.material
        
        # Shortening our Property variable names for better readability
        materialdirectory = context.scene.transmatpaths.materialdirectory
        texturedirectory = context.scene.transmatpaths.texturedirectory
        exportdirectory = context.scene.transmatpaths.exportdirectory
        
        # Setting groups to False by default
        has_groups = False
        
        # Ungrouping Group Nodes - first checks to see if there are groups, and, if so, sets has_groups to True
        for node in material.node_tree.nodes:
            if node.bl_idname == "ShaderNodeGroup":
                has_groups = True
                material.node_tree.nodes.active = node
                bpy.ops.node.group_ungroup()

################################################################################
        
        # Thanks to Jim Kroovy for this - prevents crashes with unsupported nodes
        nodes = [node for node in material.node_tree.nodes if node.bl_idname in supported_nodes]
        
        # A list of dictionaries holding the formatted strings we need to print
        uenodes = []

################################################################################
        
        print("###################### IT BEGINS! ######################")
        for node in nodes:
            
            # nodedata - is a dictionary that will update for each loop with new node data
            # 'nodename' - is a formatted string of the unique name assigned to each node
            # 'uenodename' - is the unreal equivalent of the node, eg: ShaderNodeRGB -> unreal.MaterialExpressionConstant3Vector
            # 'location' - is a formatted string of the X and Y node location values, with Y inverted, and offsets added
            # 'ID' - is the type of data we use to identify the node type - eg node.bl_idname vs node.blend_type vs node.operation
            # 'load_data' - is a list of textures and material functions to load into nodes
            # 'values' - are any numerical values that can be input to nodes: constant, RGB, etc.
            # 'connections' - are formatted strings indicating: starting node, starting socket, ending node, ending socket
            nodedata = {
            'nodename' : '',
            'uenodename' : '',
            'location' : '',
            'ID':'',
            'load_data' : [],
            'values' : [],
            'connections':[],
            }
            
            # Ignoring the Material Output, as Unreal automatically supplies the output, but not a way to connect to it!
            if not node.bl_idname == 'ShaderNodeOutputMaterial':
                
                # Gathering and formatting our basic node information - nodename,uenodename,location
                nodedata['nodename'] = str(node.name).replace('.0','').replace(' ','')
                
                # For the most part, using the bl_idname (node type) gives us the type of node we want, but 
                # whereas Blender has only one Math node, with operations selected via enum, Unreal has separate 
                # nodes for each operation, so, rather than getting the node type, we get the operation, for
                # Math nodes, and the blend type for Mix nodes
                if node.bl_idname == 'ShaderNodeMixRGB':
                    nodedata['uenodename'] = node_translate[node.blend_type]
                    nodedata['ID'] = node.blend_type
                if node.bl_idname == 'ShaderNodeMath' or node.bl_idname == 'ShaderNodeVectorMath':
                    nodedata['uenodename'] = node_translate[node.operation]
                    nodedata['ID'] = node.operation    
                if not node.bl_idname == 'ShaderNodeMixRGB' and not node.bl_idname == 'ShaderNodeMath' and not node.bl_idname == 'ShaderNodeVectorMath':
                    nodedata['uenodename'] = node_translate[node.bl_idname]
                    nodedata['ID'] = node.bl_idname
                
                # The axes in Unreal's node editor seem to be the same for X, but inverted for Y
                # I added an offset that I popped in visually, I could make this a property in the 
                # preferences panel, if the offset doesn't work for everyon    
                nodedata['location'] = str(node.location[0] - 1600) + ", " + str(node.location[1] *-1 + 1200)
                ID = nodedata['ID']
                nodename = nodedata['nodename']
                
                # Input Values - disabled for now, but could be reimplememnted by adding and attaching value, RGB nodes in place of directly setting values
#                for input in node.inputs:
#                    if not input.bl_idname == 'NodeSocketShader':
#                        if not input.is_linked:
#                                
#                            if input.type == 'VECTOR':
#                                input_name = str(f"{nodename}.{socket_translate[ID][input.name]}")
#                                input_value_0 = str(input.default_value[0])
#                                input_value_1 = str(input.default_value[1])
#                                input_value_2 = str(input.default_value[2])
#                                vector_input = str(input_name + " = " + "(" + input_value_0 + ", " + input_value_1 + ", " + input_value_2 + ")")
#                                nodedata['values'].append(vector_input)
#                                
#                            if input.type == 'RGBA':
#                                input_name = str(f"{nodename}.{socket_translate[ID][input.name]}")
#                                input_value_0 = str(input.default_value[0])
#                                input_value_1 = str(input.default_value[1])
#                                input_value_2 = str(input.default_value[2])
#                                input_value_3 = str(input.default_value[3])
#                                rgba_input = str(input_name + " = " + "(" + input_value_0 + ", " + input_value_1 + ", " + input_value_2 + ", " + input_value_3 + ")")
#                                nodedata['values'].append(rgba_input)
#                                    
#                            if not input.type == 'VECTOR' and not input.type == 'RGBA' and not input.default_value == 0:
#                                input_name = str(f"{nodename}.{socket_translate[ID][input.name]}")
#                                input_value = str(input.default_value)
#                                other_input = str(input_name + " = " + input_value)
#                                nodedata['values'].append(other_input)
                
                # Output Values are gathered for Value and RGB nodes - values
                # When making connections, Unreal requires upper case, but when
                # entering values, they must be lower case                
                if node.bl_idname == 'ShaderNodeValue':
                    output_name = str(f"{nodename}.{str(socket_translate[ID][node.outputs[0].name]).lower()}")
                    output_value = str(node.outputs[0].default_value)
                    value_output = str(output_name + " = " + output_value)
                    nodedata['values'].append(value_output)
                    
                if node.bl_idname == 'ShaderNodeRGB':
                    output_name = str(f"{nodename}.{str(socket_translate[ID][node.outputs[0].name]).lower()}")
                    output_value_0 = str(node.outputs[0].default_value[0])
                    output_value_1 = str(node.outputs[0].default_value[1])
                    output_value_2 = str(node.outputs[0].default_value[2])
                    rgb_output = str(output_name + " = " + "(" + output_value_0 + ", " + output_value_1 + ", " + output_value_2 + ")")
                    nodedata['values'].append(rgb_output)
                    
                # Material Functions and Textures - load_data
                if node.bl_idname == "ShaderNodeMixRGB" and not node.blend_type == 'MIX' or node.bl_idname == "ShaderNodeSeparateRGB" or node.bl_idname == "ShaderNodeSeparateXYZ" or node.bl_idname == "ShaderNodeSeparateHSV" or node.bl_idname == "ShaderNodeCombineRGB" or node.bl_idname == "ShaderNodeCombineXYZ" or node.bl_idname == "ShaderNodeCombineHSV":
                    mat_func = str(f"{nodename}.set_editor_property('material_function',{material_function[ID]})")    
                    nodedata['load_data'].append(mat_func)
                   
                if node.bl_idname == "ShaderNodeTexImage":
                    image_name = str(node.image.name).replace('.','_').replace(' ','')
                    texture = str(f"{nodename}.texture = unreal.load_asset('/Game{texturedirectory}/{image_name}')")
                    nodedata['load_data'].append(texture)
                
                # gathering data and formatting our Connection strings - connections
                # We only look at outputs for connections to avoid redundancy
                for output in node.outputs:
                    # Only checking outputs that are connected
                    if output.is_linked:
                        # Looping through our connections
                        for link in output.links:
                            # Ignoring our Material Output, I should probably just remove this from an earlier list to avoid this ;p
                            if not link.to_node.bl_idname == 'ShaderNodeOutputMaterial':   
                                ID = nodedata['ID']
                                nodename = nodedata['nodename']
                                from_node = str(link.from_node.name).replace('.0','').replace(' ','')
                                
                                if link.from_node.bl_idname == 'ShaderNodeRGB' or link.from_node.bl_idname == 'ShaderNodeValue':
                                    from_socket = str(f"''")
                                else:
                                    from_socket = str(f"'{socket_translate[ID][link.from_socket.name]}'")
                                
                                if link.to_node.bl_idname == 'ShaderNodeMath' or link.to_node.bl_idname == 'ShaderNodeVectorMath' or link.to_node.bl_idname == 'ShaderNodeMixShader' or link.to_node.bl_idname == 'ShaderNodeAddShader':
                                    socketnumber = re.sub("[^0-9]", "", link.to_socket.path_from_id())
                                    socketnumberint = int(socketnumber)
                                    linktonodeID = re.sub("[^0-9]", "", link.to_node.name)
                                    
                                    if linktonodeID:
                                        linktonodeIDint = int(linktonodeID)
                                        socket = str(socketnumberint - linktonodeIDint * 10)
                                    else:
                                        socket = str(socketnumberint)
                                else:           
                                    socket = link.to_socket.name
                                                
                                to_node = str(link.to_node.name).replace('.0','').replace(' ','')
                                    
                                if link.to_node.bl_idname == 'ShaderNodeMixRGB':
                                    ID = link.to_node.blend_type
                                if link.to_node.bl_idname == 'ShaderNodeMath' or link.to_node.bl_idname == 'ShaderNodeVectorMath':
                                    ID = link.to_node.operation    
                                if not link.to_node.bl_idname == 'ShaderNodeMixRGB' and not link.to_node.bl_idname == 'ShaderNodeMath' and not link.to_node.bl_idname == 'ShaderNodeVectorMath':
                                    ID = link.to_node.bl_idname
                                   
                                to_socket = str(f"'{socket_translate[ID][socket]}'")
                                
                                connection = str(nodename + "_connection = create_connection(" + from_node + ", " + from_socket+ ", " + to_node + ", " + to_socket+")")
                                nodedata['connections'].append(connection)
            
            if not node.bl_idname == 'ShaderNodeOutputMaterial':                    
                uenodes.append(nodedata)

################################################################################
# Printing
################################################################################

        # Exporting the material as a .py file to be run in Unreal
        with open(f'{exportdirectory}{material.name}_TM.py', 'w') as textoutput:
            # The file will contain all the print statements until execute
            # returns 'FINISHED'
            with redirect_stdout(textoutput):

                print("import unreal")
                print("")
                print(f"{material.name}=unreal.AssetToolsHelpers.get_asset_tools().create_asset('{material.name}','/Game/{materialdirectory}', unreal.Material, unreal.MaterialFactoryNew())")
                print(f"{material.name}.set_editor_property('use_material_attributes',True)")
                print("")
                print("create_expression = unreal.MaterialEditingLibrary.create_material_expression")
                print("create_connection = unreal.MaterialEditingLibrary.connect_material_expressions")
                print("connect_property = unreal.MaterialEditingLibrary.connect_material_property")
                print("")
                print(f"mat_func_burn = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_ColorBurn')")
                print(f"mat_func_dodge = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_ColorDodge')")
                print(f"mat_func_darken = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_Darken')")
                print(f"mat_func_difference = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_Difference')")
                print(f"mat_func_lighten = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_Lighten')")
                print(f"mat_func_linear_light = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_LinearLight')")
                print(f"mat_func_overlay = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_Overlay')")
                print(f"mat_func_screen = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_Screen')")
                print(f"mat_func_soft_light = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions03/Blends/Blend_SoftLight')")
                print(f"mat_func_separate = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions02/Utility/BreakOutFloat3Components')")
                print(f"mat_func_combine = unreal.load_asset('/Engine/Functions/Engine_MaterialFunctions02/Utility/MakeFloat3')")
                print("")
                print(f"import_tasks = []")

################################################################################

                print("")
                print("### Importing Textures")
                for node in nodes:
                    if node.bl_idname == "ShaderNodeTexImage":
                        image_name = str(node.image.name).replace('.0','').replace(' ','')
                        image_filepath = str(node.image.filepath_from_user())
                        
                        print(f"{image_name} = '{image_filepath}'")
                        print("")
                        print(f"{image_name}_import = unreal.AssetImportTask()")
                        print(f"{image_name}_import.set_editor_property('automated',True)")
                        print(f"{image_name}_import.set_editor_property('destination_path','/Game/{texturedirectory}')")
                        print(f"{image_name}_import.set_editor_property('destination_name','{image_name}')")
                        print(f"{image_name}_import.set_editor_property('factory',unreal.TextureFactory())")
                        print(f"{image_name}_import.set_editor_property('filename',{image_name})")                
                        print(f"{image_name}_import.set_editor_property('replace_existing',True)")
                        print(f"{image_name}_import.set_editor_property('save',True)")
                        print(f"import_tasks.append({image_name}_import)")
                        
                print("")
                print(f"unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(import_tasks)")

################################################################################
                
                print()
                print("### Creating Nodes")    
                for nodedata in uenodes:
                    nodename = nodedata['nodename']
                    uenodename = nodedata['uenodename']
                    location = nodedata['location']
                    
                    print(f"{nodename} = create_expression({material.name},{uenodename},{location})")
                    
                print()
                print("### Loading Material Functions and Textures")
                for nodedata in uenodes:
                    for data in nodedata['load_data']:    
                        print(data)  
                
                print()
                print("### Setting Values")
                for nodedata in uenodes:
                    for value in nodedata['values']:    
                        print(value)
                        
                print()
                print("### Creating Connections")
                for nodedata in uenodes:
                    for connection in nodedata['connections']:    
                        print(connection)
            
        if has_groups:
            bpy.ops.ed.undo()                                
        return {'FINISHED'}

################################################################################
# Panel UI
################################################################################

class TransMatPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the node editor"""
    bl_label = "TransMat v0.3.3"
    bl_idname = "BLUI_PT_transmat"
    bl_category = "TransMat"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        column = box.column()
        column.label(text="Export Directory", icon='FILE_FOLDER')
        
        row = box.row()
        row.prop(context.scene.transmatpaths, 'exportdirectory')
        
        box = layout.box()
        column = box.column()
        column.label(text="Unreal Import Subfolders", icon='FILE_FOLDER')
        
        row = box.row()
        row.prop(context.scene.transmatpaths, 'materialdirectory')
        
        row = box.row()
        row.prop(context.scene.transmatpaths, 'texturedirectory')
        
        box = layout.box()
        column = box.column()
        column.label(text="Bake noise nodes to textures", icon='NODE_SEL')
        
        row = box.row()
        row.prop(context.scene.transmatpaths, 'noiseresolution')
        
        row = box.row()
        row.operator("blui.bakenoises_operator", icon='NODE')
        
        box = layout.box()
        column = box.column()
        column.label(text="Translate Material for Unreal", icon='MATERIAL')
        
        row = box.row()
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
