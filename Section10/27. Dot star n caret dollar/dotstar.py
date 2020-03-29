import re
import os

print("Tests for different characters")

startswith = re.compile(r'^Hello')
endswith = re.compile(r'world!$')
startsandendwith = re.compile(r'^\d+$')
stringsendingwith = re.compile(r'.at')
stringsendingwithbut = re.compile(r'.at{1,2}')

mo1 = startswith.search("Hello world!")
mo2 = endswith.search("Hello world!")
mo3 = startsandendwith.search("123123123123")
mo4 = stringsendingwith.findall("The cat cato in the hat sat on the flat mat, rattat")
mo5 = stringsendingwithbut.findall("The cat in the hat sat on the flat mat, ratcoon kitkat")

print(mo1.group())
print(mo2.group())
print(mo3.group())
print(mo4)
print(mo5)

print("Name tests")
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: Al Last Name: Sweigart'))

print("greedynongreedy")

x = "<to serve humans> chicken> for dinner>"
greedy = re.compile(r'<(.*?)>')
nongreedy = re.compile(r'<(.*)>')
print(greedy.findall(x))
print(nongreedy.findall(x))
os.system("pause")

