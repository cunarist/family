import bpy  # type:ignore


class FamilySettings(bpy.types.PropertyGroup):

    duplicate_hierarchy: bpy.props.BoolProperty(
        name="Duplicate Hierarchy",
        default=True,
        description="Make object duplication operators include children",
    )
