import bpy  # type:ignore

from operators import DuplicateHierarchy, DuplicateHierarchyLinked, DeleteHierarchy

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
    bpy.utils.register_class(DuplicateHierarchy)
    bpy.utils.register_class(DuplicateHierarchyLinked)
    bpy.utils.register_class(DeleteHierarchy)

    # Adds the new operator to an existing menu.
    def job(self, context):
        self.layout.operator(DuplicateHierarchy.bl_idname)
        self.layout.operator(DuplicateHierarchyLinked.bl_idname)

    bpy.types.VIEW3D_MT_object.append(job)
    bpy.types.VIEW3D_MT_object_context_menu.append(job)


def unregister():
    bpy.utils.unregister_class(DuplicateHierarchy)
    bpy.utils.unregister_class(DuplicateHierarchyLinked)
    bpy.utils.unregister_class(DeleteHierarchy)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
