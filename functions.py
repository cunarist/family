def set_root_object_active(context, selected_objects, active_object):
    is_inside = active_object in selected_objects
    if active_object is None:
        is_parent_inside = False
    else:
        is_parent_inside = active_object.parent in selected_objects
    if not is_inside or is_parent_inside:
        for selected_object in selected_objects:
            if selected_object.parent not in selected_objects:
                context.view_layer.objects.active = selected_object


def deselect_except_root_objects(selected_objects):
    for selected_object in selected_objects:
        if selected_object.parent in selected_objects:
            selected_object.select_set(False)
