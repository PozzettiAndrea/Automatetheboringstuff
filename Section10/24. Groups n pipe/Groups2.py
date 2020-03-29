import re
import os

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search("My number is 415-555-4242")
print(mo.group())
print("this is the area code", mo.group(1))
print("this is the number:", mo.group(2))


phoneNumRegex2 = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo2 = phoneNumRegex2.search('My number is (415) 555-4242')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter)')
mo3 = batRegex.search('Batmans batmobile lost a wheel')
print(mo3.group())


os.system("pause")