import bpy  # type:ignore


class FamilySettings(bpy.types.PropertyGroup):

    duplicate_entire_hierarchy: bpy.props.BoolProperty(
        name="Duplicate Entire Hierarchy",
        default=True,
    )
