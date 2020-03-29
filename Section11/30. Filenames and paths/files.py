import os

print("Current working directory")
print(os.getcwd)
print("\n")
print("Abs path of ..")
print("os.abspath(..)")
print("\n")
print("Creating folder provaprova")
os.makedirs("Provaprova")
print("\n")
print("Filesize")
print(os.path.getsize("files.py"),os.path.getsize("files.bat"))
print("\n")
print("listdir")
print(os.listdir())
print("\n")
os.system("pause")

