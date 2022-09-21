import bpy  # type:ignore

from .operators import (
    DuplicateMove,
    DuplicateMoveLinked,
    Delete,
    DeleteSelected,
    DeleteKeepChildrenTransformation,
    DeleteHierarchy,
    SelectHierarchy,
)

from .menus import DeleteMenu

bl_info = {
    "name": "Family",
    "author": "Cunarist",
    "version": (1, 1),
    "blender": (2, 80, 0),
    "description": "An addon for Blender with duplicate and delete operations including children",
    "category": "Object",
    "doc_url": "https://cunarist.com/family",
}


def add_to_menu(self, context):
    operator = self.layout.operator(SelectHierarchy.bl_idname)
    operator.direction = "CHILD"
    operator.extend = True


def register():
    bpy.utils.register_class(DuplicateMove)
    bpy.utils.register_class(DuplicateMoveLinked)
    bpy.utils.register_class(Delete)
    bpy.utils.register_class(DeleteSelected)
    bpy.utils.register_class(DeleteKeepChildrenTransformation)
    bpy.utils.register_class(DeleteHierarchy)
    bpy.utils.register_class(SelectHierarchy)

    bpy.utils.register_class(DeleteMenu)

    bpy.types.VIEW3D_MT_object.append(add_to_menu)
    bpy.types.VIEW3D_MT_object_context_menu.append(add_to_menu)


def unregister():
    bpy.utils.unregister_class(DuplicateMove)
    bpy.utils.unregister_class(DuplicateMoveLinked)
    bpy.utils.unregister_class(Delete)
    bpy.utils.unregister_class(DeleteSelected)
    bpy.utils.unregister_class(DeleteKeepChildrenTransformation)
    bpy.utils.unregister_class(DeleteHierarchy)
    bpy.utils.unregister_class(SelectHierarchy)

    bpy.utils.unregister_class(DeleteMenu)

    bpy.types.VIEW3D_MT_object.remove(add_to_menu)
    bpy.types.VIEW3D_MT_object_context_menu.remove(add_to_menu)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
