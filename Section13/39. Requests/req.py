import requests
import os

res = requests.get("http://automatetheboringstuff.com/files/rj.txt")
print(res.status_code)
playFile = open("RomeoAndJuliet.txt", "wb")

for chunk in res.iter_content(100000):
	playFile.write(chunk)

os.system("pause")