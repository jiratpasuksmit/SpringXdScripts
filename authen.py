from jira.client import JIRA
import logging
''' 
YOUR USERNAME AND PASSWORD HERE
'''
username = ""
password = ""
jira_url = "https://jira.spring.io"


def connect_jira(log, jira_server, jira_user, jira_password):
    '''
    Connect to JIRA. Return None on error
    '''
    try:
        log.info("Connecting to JIRA: %s" % jira_server)
        jira_options = {'server': jira_server}
        jira = JIRA(options=jira_options, basic_auth=(jira_user, jira_password))
        return jira
    except Exception:
        log.error("Failed to connect to JIRA, "
                  "Please try manually login on the site, "
                  "capcha may required: %s" % Exception)
        return None


def login():
    log = logging.getLogger(__name__)
    jc = connect_jira(log, jira_url, username, password)
    return jc


