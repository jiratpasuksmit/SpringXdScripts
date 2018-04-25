import urllib.request

jira_url = "jira.spring.io"
base_url = "https://{project}/sr/jira.issueviews:searchrequest{fields}/temp/SearchRequest.csv?{query}"
file_type = ".csv"


def build_filename(project_url, count):
    from time import gmtime, strftime
    time_text = strftime("%Y%m%d_%H%M%S", gmtime())
    return project_url + "_" + time_text + "_" + str(count) + "rows" + file_type


def build_query_url(project_url, query_all_field, count):
    query_fields = "-csv-all-fields" if query_all_field else "-csv-current-fields"
    query_properties = "jqlQuery=&project=XD&tempMax={count}&status=(closed,done,resolved)".format(count=count)
    return base_url.format(project=project_url, fields=query_fields, query=query_properties)


if __name__ == '__main__':
    row_count = 100
    url = build_query_url(jira_url, True, row_count)
    test_file = urllib.request.urlretrieve(url, build_filename(jira_url, row_count))
