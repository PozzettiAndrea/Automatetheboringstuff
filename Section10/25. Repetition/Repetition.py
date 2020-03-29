import re
import os

print("Tests for ? character")

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo.group(), mo2.group())
"""Note: ? means 0 or 1 times"""

phone = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo3 = phone.search('My phone number is 555-1234')
print(mo3.group())

print("Tests for * character")

batwowoman = re.compile(r'Bat(wo)*man')
mo4 = batwowoman.search('The adventures of Batwowowowowoman')
print(mo4.group())

print("Tests for + character")

plus = re.compile(r'Bat(wo)+man')
mo5 = plus.search('The adventures of Batwoman')
print(mo5.group())
mo6 = plus.search('The adventures of Batwowowoman')
print(mo6.group())
mo7 = plus.search('The adventures of Batman')
try:
	print(mo7.group())
except:
	print("Error meep meep")

print("Tests for curly brackets")
laugh = re.compile(r'(ha){3,4}')
mo8 = laugh.search('hahahahaha')
mo9 = laugh.search('hahaha')
try:
	print(mo8.group())
except:
	print("Error meep meep")
try:
	print(mo9.group())
except:
	print("Error meep meep")
os.system("pause")

