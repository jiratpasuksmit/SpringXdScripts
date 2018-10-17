import authen
import util
import copy

actual_sp_field_name = 'Actual Story Points'
ISSUE_KEY = "issue_key"


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

        history_field_name = util.only_alphabet_lowercase(item.field)
        if history_field_name in field_name_id_list.keys():
            original_field_name = field_name_id_list[history_field_name]
        else:
            history_field_name_s = history_field_name + "s"
            original_field_name = history_field_name_s

        setattr(fields, original_field_name, item.fromString)

    return found_actual_sp_change


def run(_original_issue, _latest_issue, _field_name_id_list, _field_id_name_list):
    issue_key = _original_issue.key
    print("load " + issue_key)
    latest_fields = {}
    latest_fields.update(vars(_latest_issue.fields))
    latest_fields[ISSUE_KEY] = issue_key

    original_fields = {}
    original_fields.update(vars(extract_transitions(
        copy.deepcopy(_original_issue.fields),
        copy.deepcopy(_original_issue.changelog.histories),
        _field_name_id_list
    )))
    original_fields[ISSUE_KEY] = issue_key


    history = [latest_fields, original_fields]

    field_names = list(_field_id_name_list.keys())
    field_names.insert(0, ISSUE_KEY)
    return field_names, history

    # util.write_csv(filename="transitions_" + issue_key, field_names=field_names, data_records=history)
