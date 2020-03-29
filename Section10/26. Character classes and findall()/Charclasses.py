import re
import os

print("Tests for character classes")

lyrics = """On the twelfth day of Christmas
my true love sent to me:
12 Drummers Drumming
11 Pipers Piping
10 Lords a Leaping
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree"""

lyricsrex = re.compile(r'\d+ \w+')
mo = lyricsrex.findall(lyrics)
print(mo)

vowelclass = re.compile(r'[aeiou]')
mo2 = vowelclass.findall('robocop eats baby food A')
print(mo2)

vowelclass2 = re.compile(r'[aeiou]{2}')
mo3 = vowelclass2.findall('robocop eats baby food A')
print(mo3)


vowelclass3 = re.compile(r'[^aeiou]{2}')
mo4 = vowelclass3.findall('robocop eats baby food A')
print(mo4)

vowelclass4 = re.compile(r'[^aeiou]')
mo5 = vowelclass4.findall('robocop eats baby food A')
print(mo5)

os.system("pause")

