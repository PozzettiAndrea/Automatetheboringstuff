import os
import shelve

print("Printing example.txt")
examplefile = open("example.txt")
print(examplefile.read())
examplefile.close()

print("Adding something to a file, returns number of bytes added")
examplefile = open("bacon.txt","w")
examplefile.write("Bacon is not a vegetable \n")
examplefile.write("Duh\n")
examplefile.close()

print("Appending something to a file, returns number of bytes added")
examplefile = open("bacon.txt","a")
examplefile.write("Bacon is delicious \n")
examplefile.close()

shelfile = shelve.open('data')
shelfile["cats"] = ["Kitty", "Kat", "Bucephalus"]
shelfile.close()

shel = shelve.open("data")
print(shel["cats"])
print(list(shel.keys()))
print(list(shel.values()))

os.system("pause")

