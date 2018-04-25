username = ""
password = ""
jira_url = "jira.spring.io"
file_type = ".csv"


def build_filename(project_url, count):
    from time import gmtime, strftime
    time_text = strftime("%Y%m%d_%H%M%S", gmtime())
    return project_url + "_" + time_text + "_" + str(count) + "rows" + file_type


def write_csv(filename, field_names, data_records):
    # fieldnames = ['Application Name', 'Application ID']
    if len(data_records) == 0:
        return

    import csv
    with open(filename + '.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(field_names)
        for line in data_records:
            writer.writerow(line)


def diff_time(start, end):
    start = start[0:23]
    end = end[0:23]
    import datetime as dt
    start_dt = dt.datetime.strptime(start, '%Y-%m-%dT%H:%M:%S.%f')
    end_dt = dt.datetime.strptime(end, '%Y-%m-%dT%H:%M:%S.%f')
    diff = end_dt - start_dt
    return diff.seconds
