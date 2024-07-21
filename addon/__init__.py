import bpy
from .operators import (
    DuplicateMoveHierarchy,
    DuplicateMoveHierarchyLinked,
    ShowDeleteMenu,
    DeleteKeepChildrenTransformation,
    DeleteHierarchy,
)
from .menus import DeleteMenu
from .property_groups import FamilySettings


added_keymaps: list[tuple[bpy.types.KeyMap, bpy.types.KeyMapItem]] = []


def draw_in_3d_view_object_menu(self: bpy.types.Menu, context: bpy.types.Context):
    self.layout.separator()
    self.layout.operator(DuplicateMoveHierarchy.bl_idname)
    self.layout.operator(DuplicateMoveHierarchyLinked.bl_idname)
    self.layout.operator(DeleteKeepChildrenTransformation.bl_idname)
    self.layout.operator(DeleteHierarchy.bl_idname)


def draw_in_topbar_edit_menu(self: bpy.types.Header, context: bpy.types.Context):
    self.layout.separator()
    family_settings = getattr(context.scene, "family_settings")
    self.layout.prop(family_settings, "duplicate_hierarchy")


def register():
    bpy.utils.register_class(DuplicateMoveHierarchy)
    bpy.utils.register_class(DuplicateMoveHierarchyLinked)
    bpy.utils.register_class(ShowDeleteMenu)
    bpy.utils.register_class(DeleteKeepChildrenTransformation)
    bpy.utils.register_class(DeleteHierarchy)

    bpy.utils.register_class(DeleteMenu)
    bpy.utils.register_class(FamilySettings)

    menu = bpy.types.VIEW3D_MT_object
    menu.append(draw_in_3d_view_object_menu)
    menu = bpy.types.VIEW3D_MT_object_context_menu
    menu.append(draw_in_3d_view_object_menu)
    menu = bpy.types.TOPBAR_MT_edit
    menu.append(draw_in_topbar_edit_menu)

    setattr(
        bpy.types.Scene,
        "family_settings",
        bpy.props.PointerProperty(type=FamilySettings),
    )

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


def unregister():
    bpy.utils.unregister_class(DuplicateMoveHierarchy)
    bpy.utils.unregister_class(DuplicateMoveHierarchyLinked)
    bpy.utils.unregister_class(ShowDeleteMenu)
    bpy.utils.unregister_class(DeleteKeepChildrenTransformation)
    bpy.utils.unregister_class(DeleteHierarchy)

    bpy.utils.unregister_class(DeleteMenu)
    bpy.utils.unregister_class(FamilySettings)

    menu = bpy.types.VIEW3D_MT_object
    menu.remove(draw_in_3d_view_object_menu)
    menu = bpy.types.VIEW3D_MT_object_context_menu
    menu.remove(draw_in_3d_view_object_menu)
    menu = bpy.types.TOPBAR_MT_edit
    menu.remove(draw_in_topbar_edit_menu)

    if hasattr(bpy.types.Scene, "family_settings"):
        family_settings = getattr(bpy.types.Scene, "family_settings")
        del family_settings

    for keymap, keymap_item in added_keymaps:
        keymap.keymap_items.remove(keymap_item)
    added_keymaps.clear()
