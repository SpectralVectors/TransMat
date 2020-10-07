import bpy

# Operator Code

class TransMatOperator(bpy.types.Operator):
    """Tooltip"""
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
        
        #bpy.ops.node.select_all(action='DESELECT')
        #bpy.ops.node.select_all(action='SELECT')
        
        print("")
        print("!!!_MATERIAL START_!!!")
        
        for node in nodes:

            print("")
            # print the unique identifier first, it helps differentiate between
            # mutiple instances of the same node type, the print the bl_idname,
            # which is what we would use if we wanted to add a node of that type
            print("[Node]") 
            print(node.name + " is a " + node.bl_idname)
            
            # Determine the type of node, and what values we need to extract to
            # preserve the user's settings
            if node.bl_idname == 'ShaderNodeValue':
                print("Settings: ")
                print("Value: " + str(node.outputs[0].default_value))
            if node.bl_idname == "ShaderNodeRGB":
                print("Settings: ")
                print("RGBA: (" + 
                str(round(node.outputs[0].default_value[0], 3)) + ",",
                str(round(node.outputs[0].default_value[1], 3)) + ",",
                str(round(node.outputs[0].default_value[2], 3)) + ",",
                str(round(node.outputs[0].default_value[3], 3)) + ")")                   
            if node.bl_idname == "ShaderNodeMath":
                print("Settings: ")
                print(node.operation)
            if node.bl_idname == "ShaderNodeBsdfPrincipled":
                print("Settings: ")
                print("Base Color: (" + 
                str(round(node.inputs[0].default_value[0], 3)) + ",",
                str(round(node.inputs[0].default_value[1], 3)) + ",",
                str(round(node.inputs[0].default_value[2], 3)) + ",",
                str(round(node.inputs[0].default_value[3], 3)) + ")")
                print("Subsurface: " + 
                str(node.inputs[1].default_value))
            
            
            #looping through the outputs
            for no in node.outputs:
                # only checking those that are connected
                if no.is_linked:
                    # printing a nice, readable list of where the links start
                    # and end
                    for link in no.links:
                        links.append(link)
                        print("---Link(s)--- ")
                        print("From this node's " + link.from_socket.name + " output socket")
                        print("To the " + link.to_node.name + "'s " + link.to_socket.name + " input socket")
                        print("")
                        
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
