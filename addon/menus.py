import bpy


class DeleteMenu(bpy.types.Menu):
    bl_idname = "OBJECT_MT_delete_menu"
    bl_label = "Delete"

    def draw(self, context: bpy.types.Context | None):
        layout = self.layout

        layout.operator(
            operator="object.delete",
            text="Selected",
        )
        layout.operator(
            operator="object.delete_hierarchy",
            text="Hierarchy",
        )
