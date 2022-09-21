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
            targets.update(all_children)
        for target in targets:
            target.select_set(True)

        bpy.ops.object.duplicate(linked=False)

        # Lets Blender know the operator finished successfully.
        return {"FINISHED"}

    def invoke(self, context, event):

        returned = self.execute(context)
        bpy.ops.transform.translate("INVOKE_DEFAULT")

        return returned


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
            targets.update(all_children)
        for target in targets:
            target.select_set(True)

        bpy.ops.object.duplicate(linked=True)

        # Lets Blender know the operator finished successfully.
        return {"FINISHED"}

    def invoke(self, context, event):

        returned = self.execute(context)
        bpy.ops.transform.translate("INVOKE_DEFAULT")

        return returned


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

        for selected_object in selected_objects:
            bpy.data.objects.remove(selected_object, do_unlink=True)

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

        for selected_object in selected_objects:
            bpy.data.objects.remove(selected_object, do_unlink=True)

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

        targets = set(selected_objects)
        for selected_object in selected_objects:
            all_children = selected_object.children_recursive
            targets.update(all_children)
        for target in targets:
            bpy.data.objects.remove(target, do_unlink=True)

        # Lets Blender know the operator finished successfully.
        return {"FINISHED"}


class SelectHierarchy(bpy.types.Operator):
    # Use this as a tooltip for menu items and buttons.
    """Select children of the selected objects including themselves"""

    # Unique identifier for buttons and menu items to reference.
    bl_idname = "object.select_hierarchy"
    # Display name in the interface.
    bl_label = "Select Hierarchy"
    # Enable undo for the operator.
    bl_options = {"REGISTER", "UNDO_GROUPED"}

    direction: bpy.props.EnumProperty(
        name="Direction",
        items=[
            ("CHILD", "Select Child", "", 1),
            ("PARENT", "Select Parent", "", 2),
        ],
        default="CHILD",
    )
    extend: bpy.props.BoolProperty(
        name="Extend",
        default=True,
    )

    # execute() is called when running the operator.
    def execute(self, context):

        # The original script
        selected_objects = context.selected_objects

        if not self.extend:
            for selected_object in selected_objects:
                selected_object.select_set(False)

        targets = set()
        if self.direction == "CHILD":
            for selected_object in selected_objects:
                children = selected_object.children
                targets.update(children)
        elif self.direction == "PARENT":
            for selected_object in selected_objects:
                focus = selected_object.parent
                if focus is not None:
                    targets.add(focus)
        for target in targets:
            target.select_set(True)

        # Lets Blender know the operator finished successfully.
        return {"FINISHED"}
