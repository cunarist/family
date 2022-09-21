import bpy  # type:ignore


class DeleteMenu(bpy.types.Menu):
    bl_idname = "OBJECT_MT_delete_menu"
    bl_label = ""

    def draw(self, context):
        layout = self.layout

        text = "Delete"
        layout.operator("object.delete_selected", text=text)
        text = "Delete and Keep Children Transformation"
        layout.operator("object.delete_keep_children_transformation", text=text)
        text = "Delete Hierarchy"
        layout.operator("object.delete_hierarchy", text=text)
