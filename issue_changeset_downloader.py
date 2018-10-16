from jira import JIRA
import original_issue_extractor
import util


def get_field_name_id_list():
    _fields = jira.fields()
    field_name_id = dict()
    field_id_name = dict()
    for field in _fields:
        field_name = util.remove_space_and_special_char_lowercase(field['name'])
        field_name_id[field_name] = field['id']
        field_id_name[field['id']] = field_name
    return field_name_id, field_id_name


jira = JIRA('https://jira.spring.io')
project_name = "XD"
status = "Resolved, Done"
jql = 'project=' + project_name + ' AND status in (' + status + ') AND "Story Points" > 0 AND "Actual Story Points"  > 0'

block_size = 100
block_num = 0
while True:
    start_idx = block_num * block_size
    issues = jira.search_issues(jql, start_idx, block_size, expand="changelog,projects,issuetypes,fields,names")
    issue_field_name_id, issue_field_id_name = get_field_name_id_list()
    if len(issues) == 0:
        # Retrieve issues until there are no more to come
        break
    block_num += 1
    print("BLOCK = " + block_num.__str__())
    for fields in issues:
        # dump = json.dumps(issue.fields)
        # jsonFields = json.loads(dump)
        original_issue_extractor.run(fields, issue_field_name_id, issue_field_id_name)
        # print('%s: %s' % (issue.key, issue.fields.summary))  # import csv
