#!/usr/bin/env python3

# This is a python code to generate Pascal's Triangle in python
# Date - 23 Apr 2024
# Author : Gabriel Opiyo
# email : gabrielopiyo1133@gmail.com


from math import factorial

# for loop [main]
n = int(input("Pascal's Triangle for how many rows? "))
for i in range(n+1):
    # for loop for left spacing [adds space before printing the digit]
    for j in range(n-i+1):
        print(end=" ")
    
    #loop for printing values in row
    for k in range(i+1):
    # place here mathematical formula for Pascal's Triangle
        num = factorial(i) / (factorial(k) * factorial(i-k))
        # i = number of rows
        # k = number of columns
        print(int(num), end=" ")
    
    print()
    

