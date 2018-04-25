import authen
import util

issue_key = "XD-2638"
field_names = ['issue_key', 'date', 'developer', 'sprint_number', 'execution_time']


def get_data(key):
    jc = authen.login()
    return jc.issue(id=key, expand="changelog")


def extract_sprints(issue):
    sprints = []
    for history in issue.changelog.histories:
        for item in history.items:
            if item.field == 'Sprint':
                sprint = [issue_key,
                          history.created[0: 10],
                          history.author.displayName,
                          item.toString,
                          history.created]
                sprints.append(sprint)
    return sprints


if __name__ == '__main__':
    issue_downloaded = get_data(issue_key)
    transitions_history = extract_sprints(issue_downloaded)

    util.write_csv(filename="sprints", field_names=field_names, data_records=transitions_history)
