import bpy  # type:ignore

from .functions import set_root_object_active, deselect_except_root_objects


class DuplicateMove(bpy.types.Operator):

    "Duplicate selected objects and move them"

    bl_idname = "object.duplicate_move"
    bl_label = "Duplicate"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):

        take_hierarchy = context.scene.family_settings.duplicate_hierarchy

        selected_objects = context.selected_objects

        if len(selected_objects) == 0:
            return {"CANCELLED"}

        if take_hierarchy:
            targets = set()
            for selected_object in selected_objects:
                all_children = selected_object.children_recursive
                targets.update(all_children)
            for target in targets:
                target.select_set(True)

        bpy.ops.object.duplicate(linked=False)

        deselect_except_root_objects(context)
        set_root_object_active(context)

        return {"FINISHED"}

    def invoke(self, context, event):

        returned = self.execute(context)
        bpy.ops.transform.translate("INVOKE_DEFAULT")

        return returned


class DuplicateMoveLinked(bpy.types.Operator):

    "Duplicate selected objects, but not their object data, and move them"

    bl_idname = "object.duplicate_move_linked"
    bl_label = "Duplicate Linked"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):

        take_hierarchy = context.scene.family_settings.duplicate_hierarchy

        selected_objects = context.selected_objects

        if len(selected_objects) == 0:
            return {"CANCELLED"}

        if take_hierarchy:
            targets = set()
            for selected_object in selected_objects:
                all_children = selected_object.children_recursive
                targets.update(all_children)
            for target in targets:
                target.select_set(True)

        bpy.ops.object.duplicate(linked=True)

        deselect_except_root_objects(context)
        set_root_object_active(context)

        return {"FINISHED"}

    def invoke(self, context, event):

        returned = self.execute(context)
        bpy.ops.transform.translate("INVOKE_DEFAULT")

        return returned


class Delete(bpy.types.Operator):

    "Delete selected objects"

    bl_idname = "object.delete"
    bl_label = "Delete"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):

        selected_objects = context.selected_objects

        if len(selected_objects) == 0:
            return {"CANCELLED"}

        for selected_object in selected_objects:
            bpy.data.objects.remove(selected_object, do_unlink=True)

        return {"FINISHED"}

    def invoke(self, context, event):

        selected_objects = context.selected_objects

        if len(selected_objects) == 0:
            return {"CANCELLED"}

        bpy.ops.wm.call_menu(name="OBJECT_MT_delete_menu")

        return {"CANCELLED"}


class DeleteKeepChildrenTransformation(bpy.types.Operator):

    "Delete selected objects and keep their children's transformation"

    bl_idname = "object.delete_keep_children_transformation"
    bl_label = "Delete and Keep Children's Transformation"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):

        selected_objects = context.selected_objects

        if len(selected_objects) == 0:
            return {"CANCELLED"}

        targets = set()
        for selected_object in selected_objects:
            children = selected_object.children
            targets.update(children)
        for target in targets:
            target.select_set(True)
        bpy.ops.object.parent_clear(type="CLEAR_KEEP_TRANSFORM")
        for target in targets:
            target.select_set(False)

        for selected_object in selected_objects:
            bpy.data.objects.remove(selected_object, do_unlink=True)

        return {"FINISHED"}


class DeleteHierarchy(bpy.types.Operator):

    "Delete selected objects including their children"

    bl_idname = "object.delete_hierarchy"
    bl_label = "Delete Hierarchy"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):

        selected_objects = context.selected_objects

        if len(selected_objects) == 0:
            return {"CANCELLED"}

        targets = set(selected_objects)
        for selected_object in selected_objects:
            all_children = selected_object.children_recursive
            targets.update(all_children)
        for target in targets:
            bpy.data.objects.remove(target, do_unlink=True)

        return {"FINISHED"}


class SelectHierarchy(bpy.types.Operator):

    "Select objects up or down the hierarchy"

    bl_idname = "object.select_hierarchy"
    bl_label = "Select Hierarchy"
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

    def execute(self, context):

        selected_objects = context.selected_objects

        if len(selected_objects) == 0:
            return {"CANCELLED"}

        if not self.extend:
            for selected_object in selected_objects:
                selected_object.select_set(False)

        targets = set()
        if self.direction == "CHILD":
            for selected_object in selected_objects:
                children = selected_object.children
                if len(children) == 0:
                    targets.add(selected_object)
                else:
                    targets.update(children)
        elif self.direction == "PARENT":
            for selected_object in selected_objects:
                parent = selected_object.parent
                if parent is None:
                    targets.add(selected_object)
                else:
                    targets.add(parent)
        for target in targets:
            target.select_set(True)

        set_root_object_active(context)

        return {"FINISHED"}


class SelectAllHierarchy(bpy.types.Operator):

    "Add all children of selected objects to selection"

    bl_idname = "object.select_all_hierarchy"
    bl_label = "Select Hierarchy"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):

        selected_objects = context.selected_objects

        if len(selected_objects) == 0:
            return {"CANCELLED"}

        targets = set()
        for selected_object in selected_objects:
            all_children = selected_object.children_recursive
            targets.update(all_children)
        for target in targets:
            target.select_set(True)

        set_root_object_active(context)

        return {"FINISHED"}
