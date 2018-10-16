import authen
import util
import copy

actual_sp_field_name = 'Actual Story Points'


# def get_data(key):
#     jc = authen.login()
#     return jc.issue(id=key, expand="changelog")


def extract_transitions(fields, histories, field_name_id_list):
    for history in reversed(histories):
        should_break = revert_change(fields, history, field_name_id_list)
        if should_break:
            break
    return fields


def revert_change(fields, history, field_name_id_list):
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

        setattr(fields, original_field_name, item.fromString)

    return found_actual_sp_change


# def changeKeyIdToKeyName(proxy, _field_id_name_list):
#     dout = dict((_field_id_name_list[k.lower()], proxy[k]) for k in proxy.keys())
#     return dout


def run(_issue, _field_name_id_list, _field_id_name_list):
    issue_key = _issue.key
    latest_fields = {}
    latest_fields.update(vars(_issue.fields))

    original_fields = vars(extract_transitions(
        copy.deepcopy(_issue.fields),
        copy.deepcopy(_issue.changelog.histories),
        _field_name_id_list
    ))

    transitions_history = [latest_fields, original_fields]

    field_names = list(_field_id_name_list.keys())
    # field_names = []
    # for key in latest_fields.keys():
    #     if key in _field_id_name_list:
    #         field_names.append(_field_id_name_list[key])
    #     else:
    #         field_names.append(key)

    util.write_csv(filename="transitions_" + issue_key, field_names=field_names, data_records=transitions_history)
