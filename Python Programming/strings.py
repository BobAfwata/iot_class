#!/usr/bin/env python3

# This is a python code to demonstrate different ways to format strings in python
# Date - 23 Apr 2024
# Author : Gabriel Opiyo
# email : gabrielopiyo1133@gmail.com


name = "Gabriel"
gender = "Male"
#length is the number of characters in a string
print(len(name))
print(type(name))

#indexing a string
print(name[3])
print(name[-1])
print(name[-7])

#slicing a string [getting parts of the string]
print(name[0:3])
print(name[0:-4])
print(name[0:-5])

#concatenation is the joining of two or more strings together
f_name = "Bob"
s_name = "Afwata"
sum = f_name + " " + s_name
print(sum)

#upper() converts the string into uppercase
#lower() converts the string into lowercase

name1 = "cosmas"

name2 = "MOMBASA"


print(name1.upper())
print(name2.lower())

city = "Nairobi"
governor = "Sakaja"
print("The governor of {} is {}" .format(city, governor))
print("The governor of {1} is {0}" .format(city, governor))

print("The governor of %s is %s" .format(city, governor))

age = 20
weight = 32
print("I am {age} years old and weigh {weight} kilograms" .format(age = 21, weight = 77))

#for floats:
distance = 46.869 
print("The distance to Nairobi is {0:.2f}" .format(distance))