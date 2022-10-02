import bpy  # type:ignore

from .operators import (
    DuplicateMoveHierarchy,
    DuplicateMoveHierarchyLinked,
    ShowDeleteMenu,
    DeleteKeepChildrenTransformation,
    DeleteHierarchy,
    SelectRelated,
    SelectHierarchy,
    RelateObjects,
)
from .menus import DeleteMenu
from .property_groups import FamilySettings

bl_info = {
    "name": "Family",
    "author": "Cunarist",
    "version": (3, 0),
    "blender": (2, 80, 0),
    "description": "An addon for Blender with select, duplicate and delete operations in hierarchy",
    "category": "Object",
    "doc_url": "https://cunarist.com/family",
}

added_keymaps = []


def draw_in_3d_view_object_menu(self, context):
    self.layout.separator()
    self.layout.operator(SelectHierarchy.bl_idname)
    self.layout.operator(DuplicateMoveHierarchy.bl_idname)
    self.layout.operator(DuplicateMoveHierarchyLinked.bl_idname)
    self.layout.operator(DeleteKeepChildrenTransformation.bl_idname)
    self.layout.operator(DeleteHierarchy.bl_idname)


def draw_in_topbar_edit_menu(self, context):
    self.layout.separator()
    self.layout.prop(context.scene.family_settings, "duplicate_hierarchy")


def register():

    bpy.utils.register_class(DuplicateMoveHierarchy)
    bpy.utils.register_class(DuplicateMoveHierarchyLinked)
    bpy.utils.register_class(ShowDeleteMenu)
    bpy.utils.register_class(DeleteKeepChildrenTransformation)
    bpy.utils.register_class(DeleteHierarchy)
    bpy.utils.register_class(SelectRelated)
    bpy.utils.register_class(SelectHierarchy)
    bpy.utils.register_class(RelateObjects)

    bpy.utils.register_class(DeleteMenu)

    bpy.utils.register_class(FamilySettings)

    bpy.types.VIEW3D_MT_object.append(draw_in_3d_view_object_menu)
    bpy.types.VIEW3D_MT_object_context_menu.append(draw_in_3d_view_object_menu)
    bpy.types.TOPBAR_MT_edit.append(draw_in_topbar_edit_menu)

    bpy.types.Scene.family_settings = bpy.props.PointerProperty(type=FamilySettings)

    addon_keymaps = bpy.context.window_manager.keyconfigs.addon.keymaps

    keymap = addon_keymaps.new(
        name="Object Mode",
        space_type="EMPTY",
    )
    keymap_item = keymap.keymap_items.new(
        ShowDeleteMenu.bl_idname,
        value="PRESS",
        type="X",
    )
    added_keymaps.append((keymap, keymap_item))

    keymap = addon_keymaps.new(
        name="Object Mode",
        space_type="EMPTY",
    )
    keymap_item = keymap.keymap_items.new(
        DuplicateMoveHierarchy.bl_idname,
        value="PRESS",
        type="D",
        shift=True,
    )
    added_keymaps.append((keymap, keymap_item))

    keymap = addon_keymaps.new(
        name="Object Mode",
        space_type="EMPTY",
    )
    keymap_item = keymap.keymap_items.new(
        DuplicateMoveHierarchyLinked.bl_idname,
        value="PRESS",
        type="D",
        alt=True,
    )
    added_keymaps.append((keymap, keymap_item))

    keymap = addon_keymaps.new(
        name="Object Mode",
        space_type="EMPTY",
    )
    keymap_item = keymap.keymap_items.new(
        SelectHierarchy.bl_idname,
        value="PRESS",
        type="F",
    )
    added_keymaps.append((keymap, keymap_item))

    keymap = addon_keymaps.new(
        name="Object Mode",
        space_type="EMPTY",
    )
    keymap_item = keymap.keymap_items.new(
        RelateObjects.bl_idname,
        value="PRESS",
        type="P",
    )
    added_keymaps.append((keymap, keymap_item))


def unregister():

    bpy.utils.unregister_class(DuplicateMoveHierarchy)
    bpy.utils.unregister_class(DuplicateMoveHierarchyLinked)
    bpy.utils.unregister_class(ShowDeleteMenu)
    bpy.utils.unregister_class(DeleteKeepChildrenTransformation)
    bpy.utils.unregister_class(DeleteHierarchy)
    bpy.utils.unregister_class(SelectRelated)
    bpy.utils.unregister_class(SelectHierarchy)
    bpy.utils.unregister_class(RelateObjects)

    bpy.utils.unregister_class(DeleteMenu)

    bpy.utils.unregister_class(FamilySettings)

    bpy.types.VIEW3D_MT_object.remove(draw_in_3d_view_object_menu)
    bpy.types.VIEW3D_MT_object_context_menu.remove(draw_in_3d_view_object_menu)
    bpy.types.TOPBAR_MT_edit.remove(draw_in_topbar_edit_menu)

    if hasattr(bpy.types.Scene, "family_settings"):
        del bpy.types.Scene.family_settings

    for keymap, keymap_item in added_keymaps:
        keymap.keymap_items.remove(keymap_item)
    added_keymaps.clear()
