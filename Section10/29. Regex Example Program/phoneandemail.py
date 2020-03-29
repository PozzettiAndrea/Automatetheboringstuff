import re
import os

verbosePhone = re.compile(r'''
(
((\d\d\d)|(\(\d\d\d\)))   #area code (optional)
(\s|-)        # first dash/separator
\d\d\d   #first 3 digits
-        #second dash
\d\d\d\d #last 4 digits
(((ext(\.)?\s)\x) #extension word part (optional)
(\d{2,5}))? #extension number part (optional too)
)
''', re.VERBOSE)

verboseEmail = re.compile(r'''

[a-zA-Z0-9_.+]+ #before at
@ #At
[a-zA-Z0-9_.+]+ #after at

''', re.VERBOSE)

os.system("pause")

