import bpy

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
        links = []

        print("")
        print("!!!_MATERIAL START_!!!")
        
        for node in nodes:

            print("")
            print("[_Node_]")
            # print the unique identifier first, it helps differentiate between
            # mutiple instances of the same node type, then print the bl_idname,
            # which is what we would use if we wanted to add a node of that type 
            print(node.name + " is a " + node.bl_idname)
            # Determine the type of node, and what values we need to extract to
            # preserve the user's settings
            # Value node contains a single float
            if node.bl_idname == 'ShaderNodeValue':
                print(":::Settings::: ")
                print("Value: " + str(node.outputs[0].default_value))
            # RGB node gives 4 float values for RGBA - alpha may be unnecessary
            if node.bl_idname == "ShaderNodeRGB":
                print(":::Settings::: ")
                print("RGBA: (" + 
                str(round(node.outputs[0].default_value[0], 3)) + ",",
                str(round(node.outputs[0].default_value[1], 3)) + ",",
                str(round(node.outputs[0].default_value[2], 3)) + ",",
                str(round(node.outputs[0].default_value[3], 3)) + ")")                   
            # Math node retrieves the operation: ADD, MULTIPLY, COSINE, etc
            if node.bl_idname == "ShaderNodeMath":
                print(":::Settings::: ")
                print(node.operation)
            # Principled BSDF looks at inputs, rather than outputs
            if node.bl_idname == "ShaderNodeBsdfPrincipled":
                print(":::Settings::: ")
                print("Base Color: (" + 
                str(round(node.inputs[0].default_value[0], 3)) + ",",
                str(round(node.inputs[0].default_value[1], 3)) + ",",
                str(round(node.inputs[0].default_value[2], 3)) + ",",
                str(round(node.inputs[0].default_value[3], 3)) + ")")
                print("Metallic: " + 
                str(node.inputs[4].default_value))
                print("Specular: " + 
                str(node.inputs[5].default_value))
                print("Roughness: " + 
                str(node.inputs[7].default_value))
                print("Emission: (" + 
                str(round(node.inputs[17].default_value[0], 3)) + ",",
                str(round(node.inputs[17].default_value[1], 3)) + ",",
                str(round(node.inputs[17].default_value[2], 3)) + ",",
                str(round(node.inputs[17].default_value[3], 3)) + ")")
                print("Alpha: " + 
                str(node.inputs[18].default_value))
                print("Normal: (" + 
                str(round(node.inputs[19].default_value[0], 3)) + ",",
                str(round(node.inputs[19].default_value[1], 3)) + ",",
                str(round(node.inputs[19].default_value[2], 3)) + ")")
            
            #looping through the outputs
            for output in node.outputs:
                # only checking those that are connected
                if output.is_linked:
                    # printing a nice, readable list of where the links start
                    # and end
                    for link in output.links:
                        links.append(link)
                        print("---Link--- ")
                        print("From this node's " + link.from_socket.name + " output socket")
                        print("To the " + link.to_node.name + "'s " + link.to_socket.name + " input socket")
                        #print("")
                        
        print("")                
        print("!!!_MATERIAL END_!!!")
        print("")             
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
