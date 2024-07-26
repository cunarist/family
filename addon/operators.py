import bpy
from .property_groups import FamilySettings
from .functions import (
    set_root_object_active,
)


class DuplicateMoveHierarchy(bpy.types.Operator):
    """Duplicate selected objects, including all objects
    that are connected through a parent-child relationship,
    and move them"""

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
                parent_object = selected_object.parent
                while parent_object:
                    targets.add(parent_object)
                    targets.update(parent_object.children_recursive)
                    parent_object = parent_object.parent
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
                parent_object = selected_object.parent
                while parent_object:
                    targets.add(parent_object)
                    targets.update(parent_object.children_recursive)
                    parent_object = parent_object.parent
            for target in targets:
                target.select_set(True)

        bpy.ops.object.duplicate_move("INVOKE_DEFAULT")  # type:ignore

        set_root_object_active(context)

        return {"FINISHED"}


class DuplicateMoveHierarchyLinked(bpy.types.Operator):
    """Duplicate selected objects, including all objects
    that are connected through a parent-child relationship,
    but not their object data, and move them"""

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
                parent_object = selected_object.parent
                while parent_object:
                    targets.add(parent_object)
                    targets.update(parent_object.children_recursive)
                    parent_object = parent_object.parent
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
                parent_object = selected_object.parent
                while parent_object:
                    targets.add(parent_object)
                    targets.update(parent_object.children_recursive)
                    parent_object = parent_object.parent
            for target in targets:
                target.select_set(True)

        bpy.ops.object.duplicate_move_linked("INVOKE_DEFAULT")  # type:ignore

        set_root_object_active(context)

        return {"FINISHED"}


class ShowDeleteMenu(bpy.types.Operator):
    """Show options for performing deletion"""

    bl_idname = "object.show_delete_menu"
    bl_label = "Show Delete Menu"
    bl_options = {"MACRO"}

    def invoke(self, context: bpy.types.Context, event: bpy.types.Event):
        bpy.ops.wm.call_menu(name="OBJECT_MT_delete_menu")
        return {"FINISHED"}


class DeleteHierarchy(bpy.types.Operator):
    """Delete selected objects, including all objects
    that are connected through a parent-child relationship"""

    bl_idname = "object.delete_hierarchy"
    bl_label = "Delete Hierarchy"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context: bpy.types.Context):
        selected_objects = context.selected_objects

        if len(selected_objects) == 0:
            return {"PASS_THROUGH"}

        targets = set[bpy.types.Object]()
        for selected_object in selected_objects:
            targets.update(selected_object.children_recursive)
            parent_object = selected_object.parent
            while parent_object:
                targets.add(parent_object)
                targets.update(parent_object.children_recursive)
                parent_object = parent_object.parent
        for target in targets:
            target.select_set(True)

        bpy.ops.object.delete()

        return {"FINISHED"}
