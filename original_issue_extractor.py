import authen
import util

actual_sp_field_name = 'Actual Story Points'
issue = None
field_name_id_list = None
field_before_estimate = None


# def get_data(key):
#     jc = authen.login()
#     return jc.issue(id=key, expand="changelog")


def extract_transitions():
    global field_before_estimate
    field_before_estimate = issue.fields
    for history in reversed(issue.changelog.histories):
        should_break = revert_change(history)
        if should_break:
            break
    return field_before_estimate


def revert_change(history):
    found_actual_sp_change = False
    for item in history.items:
        if not found_actual_sp_change:
            found_actual_sp_change = item.field == actual_sp_field_name

        history_field_name = util.remove_space_and_special_char_lowercase(item.field)
        # original_field_name = field_name_id_list[history_field_name]
        if history_field_name in field_name_id_list.keys():
            original_field_name = field_name_id_list[history_field_name]
        else:
            history_field_name_s = history_field_name + "s"
            original_field_name = history_field_name_s

        global field_before_estimate
        setattr(field_before_estimate, original_field_name, item.fromString)

    return found_actual_sp_change


def run(_issue, _field_name_id_list):
    global issue
    issue = _issue
    global field_name_id_list
    field_name_id_list = _field_name_id_list

    transitions_history = extract_transitions()

    field_names = next(iter(field_name_id_list.values()))
    util.write_csv(filename="transitions_" + issue.key, field_names=field_names, data_records=transitions_history)
