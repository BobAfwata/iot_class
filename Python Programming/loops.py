#!/usr/bin/env python3

# This is a python code that demonstrates the for loop in python
# Date - 23 Apr 2024
# Author : Gabriel Opiyo
# email : gabrielopiyo1133@gmail.com


# a loop is a part of code that runs continuously
# there are 2 types of loops in Python: for loop and while loop

import math
import matplotlib.pyplot as plt
import numpy as np

# FOR loop



plt.title("Graph of sin x")

for number in range(0,10):
    print(number, end= " ")

print()

#digit = int(input("Enter the maximum number "))
# print the squares of numbers between 0 and 10
#for x in range(0, digit + 1):
#    print(x ** 2)


angles_list = np.array([]) # equivalent to x values
values_list = np.array([]) # equivalent to y values

for angle in range(0, 360, 10):
    angle_deg = math.radians(angle)
    cos_x = math.cos(angle_deg)
    angles_list = np.append(angles_list, angle_deg)
    values_list = np.append(values_list, cos_x)

plt.grid(True)
plt.plot(angles_list, values_list, color = "r") 
plt.show()



# work on printing Pascal's Triangle
# Cubes
num = int(input("Calculate the cubes of numbers from 0 to? "))
for number in range(0, num+1):
    print(number ** 3, end=" ")


