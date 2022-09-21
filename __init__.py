import bpy  # type:ignore

from .operators import (
    DuplicateHierarchy,
    DuplicateHierarchyLinked,
    Delete,
    DeleteSelected,
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

# Adds the new operator to an existing menu.
def add_to_menu(self, context):
    self.layout.operator(DuplicateHierarchy.bl_idname)
    self.layout.operator(DuplicateHierarchyLinked.bl_idname)


def register():
    bpy.utils.register_class(DuplicateHierarchy)
    bpy.utils.register_class(DuplicateHierarchyLinked)
    bpy.utils.register_class(Delete)
    bpy.utils.register_class(DeleteSelected)
    bpy.utils.register_class(DeleteHierarchy)

    bpy.utils.register_class(DeleteMenu)

    bpy.types.VIEW3D_MT_object.append(add_to_menu)
    bpy.types.VIEW3D_MT_object_context_menu.append(add_to_menu)


def unregister():
    bpy.utils.unregister_class(DuplicateHierarchy)
    bpy.utils.unregister_class(DuplicateHierarchyLinked)
    bpy.utils.unregister_class(Delete)
    bpy.utils.unregister_class(DeleteSelected)
    bpy.utils.unregister_class(DeleteHierarchy)

    bpy.utils.unregister_class(DeleteMenu)

    bpy.types.VIEW3D_MT_object.remove(add_to_menu)
    bpy.types.VIEW3D_MT_object_context_menu.remove(add_to_menu)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
