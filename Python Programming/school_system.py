#!/usr/bin/env python3

# This is a python code that implements modules to create a system circle in python
# Date - 23 Apr 2024
# Author : Gabriel Opiyo
# email : gabrielopiyo1133@gmail.com


import teacher
import students

old_age = 23

new_age = students.increase_age(old_age)

old_salary = 60000
new_salary = teacher.increase_salary(old_salary)
print(new_salary)
print(new_age)