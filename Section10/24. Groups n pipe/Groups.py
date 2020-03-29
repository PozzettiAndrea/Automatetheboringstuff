import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search("My number is 415-555-4242")
print(mo.group())
print("this is the area code", mo.group(1))
print("this is the number:", mo.group(2))


phoneNumRegex2 = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneNumRegex2.search('My number is (415) 555-4242')
print(mo.group())