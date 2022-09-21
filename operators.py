import bpy  # type:ignore


class DuplicateHierarchy(bpy.types.Operator):
    # Use this as a tooltip for menu items and buttons.
    """Duplicate selected objects including their children"""

    # Unique identifier for buttons and menu items to reference.
    bl_idname = "object.duplicate_hierarchy"
    # Display name in the interface.
    bl_label = "Duplicate Hierarchy"
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


class DuplicateHierarchyLinked(bpy.types.Operator):
    # Use this as a tooltip for menu items and buttons.
    """Duplicate linked selected objects including their children"""

    # Unique identifier for buttons and menu items to reference.
    bl_idname = "object.duplicate_hierarchy_linked"
    # Display name in the interface.
    bl_label = "Duplicate Hierarchy Linked"
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


class DeleteHierarchy(bpy.types.Operator):
    # Use this as a tooltip for menu items and buttons.
    """Delete selected objects including their children"""

    # Unique identifier for buttons and menu items to reference.
    bl_idname = "object.delete"
    # Display name in the interface.
    bl_label = "Delete Hierarchy"
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
            bpy.data.objects.remove(target, do_unlink=True)

        # Lets Blender know the operator finished successfully.
        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)
