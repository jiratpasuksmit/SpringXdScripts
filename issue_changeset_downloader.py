from jira import JIRA
import original_issue_extractor
import util
import credential

def get_field_name_id_list():
    _fields = jira.fields()
    field_name_id = dict()
    field_id_name = dict()
    for field in _fields:
        field_name = util.only_alphabet_lowercase(field['name'])
        field_name_id[field_name] = field['id']
        field_id_name[field['id']] = field_name
    return field_name_id, field_id_name


# jira = JIRA('https://jira.spring.io')
# project_name = "XD"
# jira = JIRA('https://issues.apache.org/jira')
jira = JIRA('https://jira.appcelerator.org', basic_auth=(credential.username, credential.password))
project_name = "TIMOB"
status = "Resolved, Done"
jql = 'project=' + project_name + ' AND status in (' + status + ') AND "Story Points" > 0'# AND "Actual Story Points"  > 0'

block_size = 100
block_num = 0
header_fields = None
data_list = []
while True:
    start_idx = block_num * block_size

    # just duplicate it, deepcopy sucks
    original_issues = jira.search_issues(jql, start_idx, block_size, expand="changelog")
    latest_issues = jira.search_issues(jql, start_idx, block_size, expand="changelog")

    issue_field_name_id, issue_field_id_name = get_field_name_id_list()
    if len(original_issues) == 0:
        # Retrieve issues until there are no more to come
        break
    block_num += 1
    print("BLOCK = " + block_num.__str__())

    for x in range(len(original_issues)):
        original_issue = original_issues[x]
        latest_issue = latest_issues[x]
        field_names, history = original_issue_extractor.run(original_issue, latest_issue, issue_field_name_id, issue_field_id_name)
        for item in history:
            data_list.append(item)
        header_fields = field_names
        # print('%s: %s' % (issue.key, issue.fields.summary))  # import csv

util.write_csv(filename=project_name, field_names=header_fields, data_records=data_list)
