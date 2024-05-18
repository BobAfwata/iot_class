# Read on file handling 
# https://www.w3schools.com/python/python_file_handling.asp
f = open("o.txt")
for x in f:
    print(x) # prints each line at a time

f = open("o.txt", "a") # "a" - Append [Opens a file for appending, creates the file if it does not exist]
f.write("This text is in Latin")
f.write("\n")
f.close()

f = open("o.txt", "r") # "r" - Read (Default value) [Opens a file for reading, error if file doesn't exist]
print(f.read())
f.close()

import os
if os.path.exists("p.txt"):
    os.remove("p.txt")
else:
    pass

g = open("p.txt", "x") # "x" - Create
i = 0
while i < 10:
    g.write("This is line {}" .format(i+1))
    g.write("\n")
    i += 1
g.close()
g = open("p.txt", "r")
print(g.read())
g.close()