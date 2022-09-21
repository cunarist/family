import bpy  # type:ignore

bl_info = {
    "name": "Family",
    "blender": (2, 80, 0),
    "category": "Object",
}


class DuplicateFamily(bpy.types.Operator):
    # Use this as a tooltip for menu items and buttons.
    """Duplicate selected objects including children. Similar to shift+D."""

    # Unique identifier for buttons and menu items to reference.
    bl_idname = "object.duplicate_family"
    # Display name in the interface.
    bl_label = "Duplicate Family"
    # Enable undo for the operator.
    bl_options = {"REGISTER", "UNDO"}

    # execute() is called when running the operator.
    def execute(self, context):

        # The original script
        selected_objects = context.selected_objects
        targets = []
        for selected_object in selected_objects:
            all_children = selected_object.children_recursive
            targets.append(selected_object)
            targets += all_children
        for target in targets:
            target.select_set(True)

        bpy.ops.object.duplicate(linked=False)

        # Lets Blender know the operator finished successfully.
        return {"FINISHED"}


class DuplicateFamilyLinked(bpy.types.Operator):
    # Use this as a tooltip for menu items and buttons.
    """Duplicate linked selected objects including children. Similar to alt+D."""

    # Unique identifier for buttons and menu items to reference.
    bl_idname = "object.duplicate_family_linked"
    # Display name in the interface.
    bl_label = "Duplicate Family Linked"
    # Enable undo for the operator.
    bl_options = {"REGISTER", "UNDO"}

    # execute() is called when running the operator.
    def execute(self, context):

        # The original script
        selected_objects = context.selected_objects
        targets = []
        for selected_object in selected_objects:
            all_children = selected_object.children_recursive
            targets.append(selected_object)
            targets += all_children
        for target in targets:
            target.select_set(True)

        bpy.ops.object.duplicate(linked=True)

        # Lets Blender know the operator finished successfully.
        return {"FINISHED"}


class DeleteFamily(bpy.types.Operator):
    # Use this as a tooltip for menu items and buttons.
    """Delete selected objects including children."""

    # Unique identifier for buttons and menu items to reference.
    bl_idname = "object.delete_family"
    # Display name in the interface.
    bl_label = "Delete Family"
    # Enable undo for the operator.
    bl_options = {"REGISTER", "UNDO"}

    # execute() is called when running the operator.
    def execute(self, context):

        # The original script
        selected_objects = context.selected_objects
        targets = []
        for selected_object in selected_objects:
            all_children = selected_object.children_recursive
            targets.append(selected_object)
            targets += all_children
        for target in targets:
            target.select_set(True)

        bpy.ops.object.delete()

        # Lets Blender know the operator finished successfully.
        return {"FINISHED"}


def menu_func(self, context):
    self.layout.operator(DuplicateFamily.bl_idname)
    self.layout.operator(DuplicateFamilyLinked.bl_idname)
    self.layout.operator(DeleteFamily.bl_idname)


def register():
    bpy.utils.register_class(DuplicateFamily)
    bpy.utils.register_class(DuplicateFamilyLinked)
    bpy.utils.register_class(DeleteFamily)
    # Adds the new operator to an existing menu.
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(DuplicateFamily)
    bpy.utils.unregister_class(DuplicateFamilyLinked)
    bpy.utils.unregister_class(DeleteFamily)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
