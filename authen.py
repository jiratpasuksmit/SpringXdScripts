from jira.client import JIRA
import logging
jira_url = "https://jira.spring.io"


def connect_jira(log, jira_server, jira_user, jira_password):
    '''
    Connect to JIRA. Return None on error
    '''
    try:
        log.info("Connecting to JIRA: %s" % jira_server)
        jira_options = {'server': jira_server}
        jira = JIRA(options=jira_options, basic_auth=(jira_user, jira_password))
                                        # ^--- Note the tuple
        return jira
    except Exception:
        log.error("Failed to connect to JIRA: %s" % Exception)
        return None


def login(username, password):
    log = logging.getLogger(__name__)
    jc = connect_jira(log, jira_url, username, password)
    yes = jc.search_issues(jql_str="key=XD-3745", expand="changelog", json_result=True)
    return jc

# print names of all projects
# projects = jc.projects()
# for v in projects:
#        print(v)
