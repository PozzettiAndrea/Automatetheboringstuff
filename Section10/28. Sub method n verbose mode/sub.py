import re
import os

verbose = re.compile(r'''
\d\d\d   #area code
-        # first dash
\d\d\d   #first 3 digits
-        #second dash
\d\d\d\d #last 4 digits

''', re.VERBOSE)


os.system("pause")

