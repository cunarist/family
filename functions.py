def set_root_object_active(context):

    selected_objects = context.selected_objects
    active_object = context.view_layer.objects.active

    if len(selected_objects) == 0:
        raise IndexError("there should be at least one selected object")

    is_inside = active_object in selected_objects
    if active_object is None:
        is_parent_inside = False
    else:
        is_parent_inside = active_object.parent in selected_objects

    if not is_inside or is_parent_inside:

        root_objects = set()
        ancestor_root_object = None

        for selected_object in selected_objects:
            if selected_object.parent not in selected_objects:
                root_objects.add(selected_object)

        for root_object in root_objects:
            if active_object in root_object.children_recursive:
                ancestor_root_object = root_object

        if ancestor_root_object is None:
            context.view_layer.objects.active = root_objects.pop()
        else:
            context.view_layer.objects.active = ancestor_root_object


def deselect_except_root_objects(context):

    selected_objects = context.selected_objects

    for selected_object in selected_objects:
        if selected_object.parent in selected_objects:
            selected_object.select_set(False)
