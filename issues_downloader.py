import sys

try:
    import urllib.request
except ImportError:
    import pip

    pip.main(['install', 'urllib'])
    try:
        import urllib
    except ImportError:
        sys.exit('Error ! using $ pip install urllib')

jira_url = "jira.spring.io"
base_url = "https://{project}/sr/jira.issueviews:searchrequest{fields}/temp/SearchRequest.csv?{query}"
file_type = ".csv"


def build_filename(project_url, count):
    from time import gmtime, strftime
    time_text = strftime("%Y%m%d_%H%M%S", gmtime())
    return project_url + "_" + time_text + "_" + str(count) + "rows" + file_type


def add_parameter(key, value):
    params_string = "jqlQuery="
    if type(key) is list and type(value) is list:
        for k, v in key, value:
            params_string += "&{k}={v}".format(k=k, v=v)
    else:
        params_string += "&{k}={v}".format(k=key, v=value)

    return params_string


def build_query_url(project_url, query_all_field, count):
    query_fields = "-csv-all-fields" if query_all_field else "-csv-current-fields"
    query_properties = add_parameter(["tempMax", str(count)], ["a", 123])
    return base_url.format(project=project_url, fields=query_fields, query=query_properties)


if __name__ == '__main__':
    row_count = 100
    url = build_query_url(jira_url, True, row_count)
    test_file = urllib.request.urlretrieve(url, build_filename(jira_url, row_count))
