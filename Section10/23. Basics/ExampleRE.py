import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall('Call me 415-555-1011'))