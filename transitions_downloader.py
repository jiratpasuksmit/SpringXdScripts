import authen
import util

issue_key = "XD-3745"
field_names = ['issue_key', 'developer', 'date', 'from_status', 'to_status', 'time_in_source_status', 'execution_time']


def get_data(key):
    jc = authen.login()
    return jc.issue(id=key, expand="changelog")


def extract_transitions(issue):
    status_transitions = []
    index_time = issue.fields.created
    for history in issue.changelog.histories:
        for item in history.items:
            if item.field == 'status':
                transition = [issue_key,
                              history.author.displayName,
                              history.created[0: 10],
                              item.fromString,
                              item.toString,
                              util.diff_time(index_time, history.created),
                              history.created]
                index_time = history.created
                status_transitions.append(transition)

    return status_transitions


if __name__ == '__main__':
    issue = get_data(issue_key)
    transitions_history = extract_transitions(issue)

    util.write_csv(filename="transitions", field_names=field_names, data_records=transitions_history)
