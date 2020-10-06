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
        
        for n in nodes:

            print("")
            print("[Node] " + n.name + " is a " + n.bl_idname)
            # print the unique identifier first, it helps differentiate between
            # mutiple instances of the same node type, the print the bl_idname,
            # which is what we would use if we wanted to add a node of that type
            
            
            print(material.node_tree.nodes["Value"].outputs[0].default_value)#[0])
            print(material.node_tree.nodes["RGB"].outputs[0].default_value[1])
            print(material.node_tree.nodes["RGB"].outputs[0].default_value[2])
            print(material.node_tree.nodes["RGB"].outputs[0].default_value[3])
            #print(bpy.data.materials['Material'].node_tree.nodes["RGB"].outputs[0].default_value)
            
            #looping through the outputs
            for no in n.outputs:
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
