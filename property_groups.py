import bpy


class FamilySettings(bpy.types.PropertyGroup):

    duplicate_hierarchy: bpy.props.BoolProperty(  # type: ignore
        name="Duplicate Hierarchy",
        default=True,
        description="Make object duplication operators include children",
    )
