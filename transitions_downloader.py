import json
from urllib.request import urlopen

jira_url = "jira.spring.io"
base_url = "https://{project}/rest/api/2/search?jql=key={issue_id}&expand=changelog"
file_type = ".csv"


def build_filename(project_url, count):
    from time import gmtime, strftime
    time_text = strftime("%Y%m%d_%H%M%S", gmtime())
    return project_url + "_" + time_text + "_" + str(count) + "rows" + file_type


def build_query_url(project_url, issue_id):
    return base_url.format(project=project_url, issue_id=issue_id)


if __name__ == '__main__':
    issue_id = "XD-2610"
    url = build_query_url(jira_url, issue_id)
    raw_response = urlopen(url)
    data = raw_response.read().decode("utf-8")
    data_json = json.loads(data)
    print("Y")
