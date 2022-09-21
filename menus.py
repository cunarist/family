import bpy  # type:ignore


class DeleteMenu(bpy.types.Menu):
    bl_idname = "OBJECT_MT_delete_menu"
    bl_label = ""

    def draw(self, context):
        layout = self.layout

        layout.operator("object.delete_selected", text="Delete")
        layout.operator("object.delete_hierarchy", text="Delete Hierarchy")

