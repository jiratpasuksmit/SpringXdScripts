class Project(object):
    key = ""
    url = ""
    storyPointKey = ""
    
    def __init__(self, key, url, storyPointKey):
        self.key = key
        self.url = url
        self.storyPointKey = storyPointKey


STORY_POINTS = 'Story Points'
projectList = \
    {
        Project('XD', 'https://jira.spring.io', STORY_POINTS),
        # Project('MESOS', 'https://issues.apache.org/jira', STORY_POINTS),
        # Project('USERGRID', 'https://jira.apache.org/jira', STORY_POINTS),
        # Project('TISTUD', 'https://jira.appcelerator.org', STORY_POINTS),
        # Project('APSTUD', 'https://jira.appcelerator.org', STORY_POINTS),
        # Project('TIMOB', 'https://jira.appcelerator.org', STORY_POINTS),
        # Project('BAM', 'https://jira.atlassian.com', STORY_POINTS),
        # Project('CLOV', 'https://jira.atlassian.com', STORY_POINTS),
        # Project('MDL', 'https://tracker.moodle.org', 'Story Points (Obsolete)'),
        # Project('DM', 'https://jira.lsstcorp.org', STORY_POINTS),
        # Project('MULE', 'https://www.mulesoft.org/jira/', STORY_POINTS),
        # Project('TDQ', 'https://jira.talendforge.org', STORY_POINTS),
        # Project('TESB', 'https://jira.talendforge.org', STORY_POINTS)
    }
