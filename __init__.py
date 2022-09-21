import bpy  # type:ignore

from .operators import (
    DuplicateMove,
    DuplicateMoveLinked,
    Delete,
    DeleteSelected,
    DeleteKeepChildrenTransformation,
    DeleteHierarchy,
    SelectHierarchy,
    SelectHierarchySimple,
)

from .menus import DeleteMenu

from .property_groups import FamilySettings

bl_info = {
    "name": "Family",
    "author": "Cunarist",
    "version": (1, 5),
    "blender": (2, 80, 0),
    "description": "An addon for Blender with duplicate and delete operations including children",
    "category": "Object",
    "doc_url": "https://cunarist.com/family",
}


def draw_in_3d_view_object_menu(self, context):
    self.layout.separator()
    self.layout.operator(SelectHierarchySimple.bl_idname)


def draw_in_topbar_edit_menu(self, context):
    self.layout.separator()
    self.layout.prop(context.scene.family_settings, "duplicate_hierarchy")


def register():
    bpy.utils.register_class(DuplicateMove)
    bpy.utils.register_class(DuplicateMoveLinked)
    bpy.utils.register_class(Delete)
    bpy.utils.register_class(DeleteSelected)
    bpy.utils.register_class(DeleteKeepChildrenTransformation)
    bpy.utils.register_class(DeleteHierarchy)
    bpy.utils.register_class(SelectHierarchy)
    bpy.utils.register_class(SelectHierarchySimple)

    bpy.utils.register_class(DeleteMenu)

    bpy.utils.register_class(FamilySettings)

    bpy.types.VIEW3D_MT_object.append(draw_in_3d_view_object_menu)
    bpy.types.VIEW3D_MT_object_context_menu.append(draw_in_3d_view_object_menu)
    bpy.types.TOPBAR_MT_edit.append(draw_in_topbar_edit_menu)

    bpy.types.Scene.family_settings = bpy.props.PointerProperty(type=FamilySettings)


def unregister():
    bpy.utils.unregister_class(DuplicateMove)
    bpy.utils.unregister_class(DuplicateMoveLinked)
    bpy.utils.unregister_class(Delete)
    bpy.utils.unregister_class(DeleteSelected)
    bpy.utils.unregister_class(DeleteKeepChildrenTransformation)
    bpy.utils.unregister_class(DeleteHierarchy)
    bpy.utils.unregister_class(SelectHierarchy)
    bpy.utils.unregister_class(SelectHierarchySimple)

    bpy.utils.unregister_class(DeleteMenu)

    bpy.utils.unregister_class(FamilySettings)

    bpy.types.VIEW3D_MT_object.remove(draw_in_3d_view_object_menu)
    bpy.types.VIEW3D_MT_object_context_menu.remove(draw_in_3d_view_object_menu)
    bpy.types.TOPBAR_MT_edit.remove(draw_in_topbar_edit_menu)

    del bpy.types.Scene.family_settings


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
