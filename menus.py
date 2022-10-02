import bpy  # type:ignore


class DeleteMenu(bpy.types.Menu):
    bl_idname = "OBJECT_MT_delete_menu"
    bl_label = "Delete"

    def draw(self, context):
        layout = self.layout

        layout.operator(
            operator="object.delete",
            text="Selected",
        )
        layout.operator(
            operator="object.delete_keep_children_transformation",
            text="Selected (Keep Children's Transformation)",
        )
        layout.operator(
            operator="object.delete_hierarchy",
            text="Hierarchy",
        )
