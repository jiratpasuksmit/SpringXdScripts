# SpringXdScripts
Script to download issues report and extract its properties

What you can do with these scripts

Download issues, run 'issues_downloader.py'.
Customizable properties
- Query Properties
- Query fields (all or current)
- Row count (less than 1000)

Extract transitions of an issue (Require Login credentials), run 'transitions_downloader.py'
Customizable properties
- Issue key

Extract sprint of an issue (Require Login credentials), run 'sprints_downloader.py'
Customizable properties
- Issue key

Login
* Username and Password using for Login should set at authen.py (username & password)
* successful Login should return nothing

FUTURE TASK
- implement OAUTH to prevent request rejection (occured sometime)
