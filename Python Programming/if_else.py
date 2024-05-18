#!/usr/bin/env python3

# This is a python code to demonstrate if and else conditions in python
# Date - 17 Apr 2024
# Author : Gabriel Opiyo
# email : gabrielopiyo1133@gmail.com

age = int(input("Enter your age: "))
weight = int(input("Enter your weight: "))


if age <= 10:
    print("You should be in primary school")
elif age >= 17 and  weight >= 50 and weight <70 :
    print("You should be in high school , playing football ")
elif age >=17 or weight >=70:
    print("You should be in high school , playing rugby")
else:
    print("You should be in college")



