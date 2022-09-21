import bpy  # type:ignore


class DuplicateMove(bpy.types.Operator):
    # Use this as a tooltip for menu items and buttons.
    """Duplicate the selected objects including their children and move them"""

    # Unique identifier for buttons and menu items to reference.
    bl_idname = "object.duplicate_move"
    # Display name in the interface.
    bl_label = "Duplicate"
    # Enable undo for the operator.
    bl_options = {"REGISTER", "UNDO"}

    # execute() is called when running the operator.
    def execute(self, context):

        # The original script
        selected_objects = context.selected_objects

        targets = set()
        for selected_object in selected_objects:
            all_children = selected_object.children_recursive
            targets.add(selected_object)
            targets.update(all_children)
        for target in targets:
            target.select_set(True)

        bpy.ops.object.duplicate(linked=False)
        bpy.ops.transform.translate("INVOKE_DEFAULT")

        # Lets Blender know the operator finished successfully.
        return {"FINISHED"}


class DuplicateMoveLinked(bpy.types.Operator):
    # Use this as a tooltip for menu items and buttons.
    """Duplicate the selected objects including their children, but not their object data, and move them"""

    # Unique identifier for buttons and menu items to reference.
    bl_idname = "object.duplicate_move_linked"
    # Display name in the interface.
    bl_label = "Duplicate Linked"
    # Enable undo for the operator.
    bl_options = {"REGISTER", "UNDO"}

    # execute() is called when running the operator.
    def execute(self, context):

        # The original script
        selected_objects = context.selected_objects

        targets = set()
        for selected_object in selected_objects:
            all_children = selected_object.children_recursive
            targets.add(selected_object)
            targets.update(all_children)
        for target in targets:
            target.select_set(True)

        bpy.ops.object.duplicate(linked=True)
        bpy.ops.transform.translate("INVOKE_DEFAULT")

        # Lets Blender know the operator finished successfully.
        return {"FINISHED"}


class Delete(bpy.types.Operator):
    # Use this as a tooltip for menu items and buttons.
    """Show delete menu"""

    # Unique identifier for buttons and menu items to reference.
    bl_idname = "object.delete"
    # Display name in the interface.
    bl_label = "Delete"
    # Enable undo for the operator.
    bl_options = set()

    # execute() is called when running the operator.
    def execute(self, context):

        bpy.ops.wm.call_menu(name="OBJECT_MT_delete_menu")

        # Lets Blender know the operator finished successfully.
        return {"FINISHED"}


class DeleteSelected(bpy.types.Operator):
    # Use this as a tooltip for menu items and buttons.
    """Delete the selected objects"""

    # Unique identifier for buttons and menu items to reference.
    bl_idname = "object.delete_selected"
    # Display name in the interface.
    bl_label = "Delete Selected"
    # Enable undo for the operator.
    bl_options = {"REGISTER", "UNDO"}

    # execute() is called when running the operator.
    def execute(self, context):

        # The original script
        selected_objects = context.selected_objects

        targets = selected_objects
        for target in targets:
            bpy.data.objects.remove(target, do_unlink=True)

        # Lets Blender know the operator finished successfully.
        return {"FINISHED"}


class DeleteKeepChildrenTransformation(bpy.types.Operator):
    # Use this as a tooltip for menu items and buttons.
    """Delete the selected objects and keep children's transformation"""

    # Unique identifier for buttons and menu items to reference.
    bl_idname = "object.delete_keep_children_transformation"
    # Display name in the interface.
    bl_label = "Delete and Keep Children's Transformation"
    # Enable undo for the operator.
    bl_options = {"REGISTER", "UNDO"}

    # execute() is called when running the operator.
    def execute(self, context):

        # The original script
        selected_objects = context.selected_objects

        targets = set()
        for selected_object in selected_objects:
            children = selected_object.children
            targets.update(children)
        for target in targets:
            target.select_set(True)
        bpy.ops.object.parent_clear(type="CLEAR_KEEP_TRANSFORM")

        targets = selected_objects
        for target in targets:
            bpy.data.objects.remove(target, do_unlink=True)

        # Lets Blender know the operator finished successfully.
        return {"FINISHED"}


class DeleteHierarchy(bpy.types.Operator):
    # Use this as a tooltip for menu items and buttons.
    """Delete the selected objects including their children"""

    # Unique identifier for buttons and menu items to reference.
    bl_idname = "object.delete_hierarchy"
    # Display name in the interface.
    bl_label = "Delete Hierarchy"
    # Enable undo for the operator.
    bl_options = {"REGISTER", "UNDO"}

    # execute() is called when running the operator.
    def execute(self, context):

        # The original script
        selected_objects = context.selected_objects

        targets = set()
        for selected_object in selected_objects:
            all_children = selected_object.children_recursive
            targets.add(selected_object)
            targets.update(all_children)
        for target in targets:
            bpy.data.objects.remove(target, do_unlink=True)

        # Lets Blender know the operator finished successfully.
        return {"FINISHED"}
