#!/usr/bin/env python3

# This is a python code to calculate tax in python
# Date - 23 Apr 2024
# Author : Gabriel Opiyo
# email : gabrielopiyo1133@gmail.com


salary = int(input("Enter your salary: "))
if salary < 0:
    print("Invalid input")
elif salary <= 50000:
    tax = 0.15 * salary
    print("You should pay tax of KES {}".format(tax))
elif salary > 50000 and salary <= 70000:
    tax = 0.18 * salary
    print("You should pay tax of KES {}".format(tax))
else:
    tax = 0.20 * salary
    print("You should pay tax of KES {}".format(tax))


