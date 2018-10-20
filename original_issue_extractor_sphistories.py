import authen
import util
import copy

sp_field_name = 'Story Points'
ISSUE_KEY = "_issue_key"
HISTORIC_TYPE = "_historic_type"
HISTORIC_TYPE_BEFORE = "before"
HISTORIC_TYPE_LATEST = "latest"


# def get_data(key):
#     jc = authen.login()
#     return jc.issue(id=key, expand="changelog")


def extract_transitions(fields, histories, field_name_id_list):
    firstSpChange = None
    for history in histories:
        if isSpChange(history):
            if firstSpChange is None:
                firstSpChange = history

    for history in reversed(histories):
        revert_change(fields, history, field_name_id_list)
        if history == firstSpChange:
            break
    return fields


def revert_change(fields, history, field_name_id_list):
    for item in history.items:

        history_field_name = util.only_alphabet_lowercase(item.field)
        if history_field_name in field_name_id_list.keys():
            original_field_name = field_name_id_list[history_field_name]
        else:
            history_field_name_s = history_field_name + "s"
            original_field_name = history_field_name_s

        setattr(fields, original_field_name, item.fromString)


def isSpChange(history):
    for item in history.items:
        if item.field == sp_field_name:
            return True

    return False


def convertToReadableDict(fields, _field_id_name_list):
    fieldsDict = {}
    fieldsDict.update(vars(fields))

    newDict = {}
    for key in fieldsDict.keys():
        try:
            newDict[_field_id_name_list[key.lower()]] = fieldsDict[key]
        except Exception:
            printIfNotInSafeList(key, fieldsDict[key])
    return newDict


def run(_original_issue, _latest_issue, _field_name_id_list, _field_id_name_list):
    issue_key = _original_issue.key
    print("load " + issue_key)
    latestFields = convertToReadableDict(_latest_issue.fields, _field_id_name_list)
    latestFields[ISSUE_KEY] = issue_key
    latestFields[HISTORIC_TYPE] = HISTORIC_TYPE_LATEST

    originalFields = convertToReadableDict(extract_transitions(
        copy.deepcopy(_original_issue.fields),
        copy.deepcopy(_original_issue.changelog.histories),
        _field_name_id_list
    ), _field_id_name_list)

    originalFields[ISSUE_KEY] = issue_key
    originalFields[HISTORIC_TYPE] = HISTORIC_TYPE_BEFORE

    history = [latestFields, originalFields]

    field_names = list(latestFields.keys())
    field_names.insert(0, ISSUE_KEY)
    field_names.insert(1, HISTORIC_TYPE)
    return field_names, history

    # util.write_csv(filename="transitions_" + issue_key, field_names=field_names, data_records=history)


mesosSafeList = ['links', 'workflows']

def printIfNotInSafeList(key, value):
    if key not in [
        '__module__',
        '__dict__',
        '__weakref__',
        '__doc__',
        '__module__',
        '__dict__',
        '__weakref__',
        '__doc__',
    ] and key not in mesosSafeList:
        print("cant find key = " + key + " with value " + str(value))

