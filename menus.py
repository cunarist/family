import bpy  # type:ignore


class DeleteMenu(bpy.types.Menu):
    bl_idname = "OBJECT_MT_delete_menu"
    bl_label = ""

    def draw(self, context):
        layout = self.layout

        layout.operator("object.delete_simple")
        layout.operator("object.delete_keep_children_transformation")
        layout.operator("object.delete_hierarchy")
