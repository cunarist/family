import bpy
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

__all__ = []

bl_info = {
    "name": "Family",
    "author": "Cunarist",
    "version": (3, 3),
    "blender": (3, 0, 0),
    "description": "An addon for Blender with select, duplicate and delete operations in hierarchy",
    "category": "Object",
    "doc_url": "https://cunarist.com/family",
}

added_keymaps = []


def draw_in_3d_view_object_menu(self: bpy.types.Menu, context: bpy.types.Context):
    self.layout.separator()
    self.layout.operator(SelectHierarchy.bl_idname)
    self.layout.operator(DuplicateMoveHierarchy.bl_idname)
    self.layout.operator(DuplicateMoveHierarchyLinked.bl_idname)
    self.layout.operator(DeleteKeepChildrenTransformation.bl_idname)
    self.layout.operator(DeleteHierarchy.bl_idname)


def draw_in_topbar_edit_menu(self: bpy.types.Header, context: bpy.types.Context):
    self.layout.separator()
    family_settings = getattr(context.scene, "family_settings")
    self.layout.prop(family_settings, "duplicate_hierarchy")


def register():
    bpy.utils.register_class(DuplicateMoveHierarchy)  # type: ignore
    bpy.utils.register_class(DuplicateMoveHierarchyLinked)  # type: ignore
    bpy.utils.register_class(ShowDeleteMenu)  # type: ignore
    bpy.utils.register_class(DeleteKeepChildrenTransformation)  # type: ignore
    bpy.utils.register_class(DeleteHierarchy)  # type: ignore
    bpy.utils.register_class(SelectRelated)  # type: ignore
    bpy.utils.register_class(SelectHierarchy)  # type: ignore
    bpy.utils.register_class(RelateObjects)  # type: ignore

    bpy.utils.register_class(DeleteMenu)  # type: ignore

    bpy.utils.register_class(FamilySettings)  # type: ignore

    menu = bpy.types.VIEW3D_MT_object
    menu.append(draw_in_3d_view_object_menu)  # type: ignore
    menu = bpy.types.VIEW3D_MT_object_context_menu
    menu.append(draw_in_3d_view_object_menu)  # type: ignore
    menu = bpy.types.TOPBAR_MT_edit
    menu.append(draw_in_topbar_edit_menu)  # type: ignore

    setattr(
        bpy.types.Scene,
        "family_settings",
        bpy.props.PointerProperty(type=FamilySettings),  # type: ignore
    )

    addon_keymaps = bpy.context.window_manager.keyconfigs.addon.keymaps  # type: ignore

    keymap = addon_keymaps.new(  # type: ignore
        name="Object Mode",
        space_type="EMPTY",
    )
    keymap_item = keymap.keymap_items.new(  # type: ignore
        ShowDeleteMenu.bl_idname,
        value="PRESS",
        type="X",
    )
    added_keymaps.append((keymap, keymap_item))  # type: ignore

    keymap = addon_keymaps.new(  # type: ignore
        name="Object Mode",
        space_type="EMPTY",
    )
    keymap_item = keymap.keymap_items.new(  # type: ignore
        DuplicateMoveHierarchy.bl_idname,
        value="PRESS",
        type="D",
        shift=True,
    )
    added_keymaps.append((keymap, keymap_item))  # type: ignore

    keymap = addon_keymaps.new(  # type: ignore
        name="Object Mode",
        space_type="EMPTY",
    )
    keymap_item = keymap.keymap_items.new(  # type: ignore
        DuplicateMoveHierarchyLinked.bl_idname,
        value="PRESS",
        type="D",
        alt=True,
    )
    added_keymaps.append((keymap, keymap_item))  # type: ignore

    keymap = addon_keymaps.new(  # type: ignore
        name="Object Mode",
        space_type="EMPTY",
    )
    keymap_item = keymap.keymap_items.new(  # type: ignore
        SelectHierarchy.bl_idname,
        value="PRESS",
        type="F",
        ctrl=True,
    )
    added_keymaps.append((keymap, keymap_item))  # type: ignore

    keymap = addon_keymaps.new(  # type: ignore
        name="Object Mode",
        space_type="EMPTY",
    )
    keymap_item = keymap.keymap_items.new(  # type: ignore
        RelateObjects.bl_idname,
        value="PRESS",
        type="P",
    )
    added_keymaps.append((keymap, keymap_item))  # type: ignore


def unregister():
    bpy.utils.unregister_class(DuplicateMoveHierarchy)  # type: ignore
    bpy.utils.unregister_class(DuplicateMoveHierarchyLinked)  # type: ignore
    bpy.utils.unregister_class(ShowDeleteMenu)  # type: ignore
    bpy.utils.unregister_class(DeleteKeepChildrenTransformation)  # type: ignore
    bpy.utils.unregister_class(DeleteHierarchy)  # type: ignore
    bpy.utils.unregister_class(SelectRelated)  # type: ignore
    bpy.utils.unregister_class(SelectHierarchy)  # type: ignore
    bpy.utils.unregister_class(RelateObjects)  # type: ignore

    bpy.utils.unregister_class(DeleteMenu)  # type: ignore

    bpy.utils.unregister_class(FamilySettings)  # type: ignore

    menu = bpy.types.VIEW3D_MT_object
    menu.remove(draw_in_3d_view_object_menu)  # type: ignore
    menu = bpy.types.VIEW3D_MT_object_context_menu
    menu.remove(draw_in_3d_view_object_menu)  # type: ignore
    menu = bpy.types.TOPBAR_MT_edit
    menu.remove(draw_in_topbar_edit_menu)  # type: ignore

    if hasattr(bpy.types.Scene, "family_settings"):
        family_settings = getattr(bpy.types.Scene, "family_settings")
        del family_settings

    keymap: bpy.types.KeyMap
    keymap_item: bpy.types.KeyMapItem
    for keymap, keymap_item in added_keymaps:
        keymap.keymap_items.remove(keymap_item)  # type: ignore
    added_keymaps.clear()
