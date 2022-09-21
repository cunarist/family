import bpy  # type:ignore

from .operators import (
    DuplicateMove,
    DuplicateMoveLinked,
    Delete,
    DeleteSelected,
    DeleteKeepChildrenTransformation,
    DeleteHierarchy,
)

from .menus import DeleteMenu

bl_info = {
    "name": "Family",
    "author": "Cunarist",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "description": "An addon for Blender with duplicate and delete operations including children",
    "category": "Object",
    "doc_url": "https://cunarist.com/family",
}


def register():
    bpy.utils.register_class(DuplicateMove)
    bpy.utils.register_class(DuplicateMoveLinked)
    bpy.utils.register_class(Delete)
    bpy.utils.register_class(DeleteSelected)
    bpy.utils.register_class(DeleteKeepChildrenTransformation)
    bpy.utils.register_class(DeleteHierarchy)

    bpy.utils.register_class(DeleteMenu)


def unregister():
    bpy.utils.unregister_class(DuplicateMove)
    bpy.utils.unregister_class(DuplicateMoveLinked)
    bpy.utils.unregister_class(Delete)
    bpy.utils.unregister_class(DeleteSelected)
    bpy.utils.unregister_class(DeleteKeepChildrenTransformation)
    bpy.utils.unregister_class(DeleteHierarchy)

    bpy.utils.unregister_class(DeleteMenu)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
