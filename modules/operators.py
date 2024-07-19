import bpy
from .property_groups import FamilySettings
from .functions import (
    set_root_object_active,
)


class DuplicateMoveHierarchy(bpy.types.Operator):
    """
    Duplicate selected objects with all their recursive children and move them
    """

    bl_idname = "object.duplicate_move_hierarchy"
    bl_label = "Duplicate Hierarchy"
    bl_options = {"MACRO"}

    def execute(self, context: bpy.types.Context):
        family_settings: FamilySettings = getattr(context.scene, "family_settings")
        take_hierarchy = family_settings.duplicate_hierarchy
        selected_objects = context.selected_objects

        if take_hierarchy:
            targets = set[bpy.types.Object]()
            for selected_object in selected_objects:
                targets.update(selected_object.children_recursive)
            for target in targets:
                target.select_set(True)

        bpy.ops.object.duplicate_move()

        set_root_object_active(context)

        return {"FINISHED"}

    def invoke(self, context: bpy.types.Context, event: bpy.types.Event):
        family_settings: FamilySettings = getattr(context.scene, "family_settings")
        take_hierarchy = family_settings.duplicate_hierarchy
        selected_objects = context.selected_objects

        if take_hierarchy:
            targets = set[bpy.types.Object]()
            for selected_object in selected_objects:
                targets.update(selected_object.children_recursive)
            for target in targets:
                target.select_set(True)

        bpy.ops.object.duplicate_move("INVOKE_DEFAULT")  # type:ignore

        set_root_object_active(context)

        return {"FINISHED"}


class DuplicateMoveHierarchyLinked(bpy.types.Operator):
    """
    Duplicate selected objects with all their recursive children,
    but not their object data, and move them
    """

    bl_idname = "object.duplicate_move_hierarchy_linked"
    bl_label = "Duplicate Hierarchy Linked"
    bl_options = {"MACRO"}

    def execute(self, context: bpy.types.Context):
        family_settings: FamilySettings = getattr(context.scene, "family_settings")
        take_hierarchy = family_settings.duplicate_hierarchy
        selected_objects = context.selected_objects

        if take_hierarchy:
            targets = set[bpy.types.Object]()
            for selected_object in selected_objects:
                targets.update(selected_object.children_recursive)
            for target in targets:
                target.select_set(True)

        bpy.ops.object.duplicate_move_linked()

        set_root_object_active(context)

        return {"FINISHED"}

    def invoke(self, context: bpy.types.Context, event: bpy.types.Event):
        family_settings: FamilySettings = getattr(context.scene, "family_settings")
        take_hierarchy = family_settings.duplicate_hierarchy
        selected_objects = context.selected_objects

        if take_hierarchy:
            targets = set[bpy.types.Object]()
            for selected_object in selected_objects:
                targets.update(selected_object.children_recursive)
            for target in targets:
                target.select_set(True)

        bpy.ops.object.duplicate_move_linked("INVOKE_DEFAULT")  # type:ignore

        set_root_object_active(context)

        return {"FINISHED"}


class ShowDeleteMenu(bpy.types.Operator):
    """
    Show options for performing deletion
    """

    bl_idname = "object.show_delete_menu"
    bl_label = "Show Delete Menu"
    bl_options = {"MACRO"}

    def invoke(self, context: bpy.types.Context, event: bpy.types.Event):
        bpy.ops.wm.call_menu(name="OBJECT_MT_delete_menu")
        return {"FINISHED"}


class DeleteKeepChildrenTransformation(bpy.types.Operator):
    """
    Delete selected objects and keep their children's transformation
    """

    bl_idname = "object.delete_keep_children_transformation"
    bl_label = "Delete and Keep Children's Transformation"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context: bpy.types.Context):
        selected_objects = context.selected_objects

        if len(selected_objects) == 0:
            return {"PASS_THROUGH"}

        targets = set[bpy.types.Object]()
        for selected_object in selected_objects:
            targets.update(selected_object.children)
        for target in targets:
            target.select_set(True)
        bpy.ops.object.parent_clear(type="CLEAR_KEEP_TRANSFORM")
        for target in targets:
            target.select_set(False)

        for selected_object in selected_objects:
            selected_object.select_set(True)

        bpy.ops.object.delete()

        return {"FINISHED"}


class DeleteHierarchy(bpy.types.Operator):
    """
    Delete selected objects including all their recursive children
    """

    bl_idname = "object.delete_hierarchy"
    bl_label = "Delete Hierarchy"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context: bpy.types.Context):
        selected_objects = context.selected_objects

        if len(selected_objects) == 0:
            return {"PASS_THROUGH"}

        targets: set[bpy.types.Object] = set(selected_objects)
        for selected_object in selected_objects:
            targets.update(selected_object.children_recursive)
        for target in targets:
            target.select_set(True)

        bpy.ops.object.delete()

        return {"FINISHED"}


class SelectRelated(bpy.types.Operator):
    """
    Select objects up or down the hierarchy
    """

    bl_idname = "object.select_hierarchy"
    bl_label = "Select Related"
    bl_options = {"REGISTER", "UNDO_GROUPED"}

    direction_items = [
        ("CHILD", "Select Child", "", 1),
        ("PARENT", "Select Parent", "", 2),
    ]
    direction: bpy.props.EnumProperty(
        name="Direction",
        items=direction_items,
        default="CHILD",
    )  # type:ignore
    extend: bpy.props.BoolProperty(
        name="Extend",
        default=True,
    )  # type:ignore

    def execute(self, context: bpy.types.Context):
        selected_objects = context.selected_objects

        if len(selected_objects) == 0:
            return {"PASS_THROUGH"}

        if not self.extend:
            for selected_object in selected_objects:
                selected_object.select_set(False)

        targets = set[bpy.types.Object]()
        if self.direction == "CHILD":
            for selected_object in selected_objects:
                children = list(selected_object.children)
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


class SelectHierarchy(bpy.types.Operator):
    """
    Add all recursive children of selected objects to selection
    """

    bl_idname = "object.select_real_hierarchy"
    bl_label = "Select Hierarchy"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context: bpy.types.Context):
        selected_objects = context.selected_objects

        if len(selected_objects) == 0:
            return {"PASS_THROUGH"}

        targets = set[bpy.types.Object]()
        for selected_object in selected_objects:
            targets.update(selected_object.children_recursive)
        for target in targets:
            target.select_set(True)

        set_root_object_active(context)

        return {"FINISHED"}


class RelateObjects(bpy.types.Operator):
    """
    Make parent-child relationship keeping children's transform
    if objects other than the active one are selected,
    otherwise remove parent-child relationship keeping children's transform
    """

    bl_idname = "object.relate_objects"
    bl_label = "Relate Objects"
    bl_options = {"REGISTER", "UNDO_GROUPED"}

    def execute(self, context: bpy.types.Context):
        selected_objects = context.selected_objects
        active_object = context.view_layer.objects.active

        if active_object is None:
            return {"PASS_THROUGH"}

        create_relationship = False
        for selected_object in selected_objects:
            if selected_object is not active_object:
                create_relationship = True
                break

        if create_relationship:
            should_clear_parent_on_active = False
            for selected_object in selected_objects:
                if active_object in selected_object.children_recursive:
                    should_clear_parent_on_active = True
                    break
            if should_clear_parent_on_active:
                for selected_object in selected_objects:
                    selected_object.select_set(False)
                active_object.select_set(True)
                bpy.ops.object.parent_clear(type="CLEAR_KEEP_TRANSFORM")
                for selected_object in selected_objects:
                    selected_object.select_set(True)
            bpy.ops.object.parent_set(keep_transform=True)
            for selected_object in selected_objects:
                selected_object.select_set(False)
            active_object.select_set(True)
        else:
            active_object.select_set(False)
            children = list(active_object.children)
            for child in children:
                child.select_set(True)
            bpy.ops.object.parent_clear(type="CLEAR_KEEP_TRANSFORM")

        return {"FINISHED"}
