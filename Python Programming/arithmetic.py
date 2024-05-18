#!/usr/bin/env python3

# This is a python code to demonstrate arithmetic operators in python
# Date - 12 Apr 2024
# Author : Gabriel Opiyo
# email : gabrielopiyo1133@gmail.com


import math
import matplotlib

x = 7
y = 3
sum = x + y
diff = x - y
prod = x * y
quotient = x / y
mod = x % y

# x raised to power y
power = x ** y

print("sum = {}, diff = {}, prod = {}, quotient = {} modulus = {}, power = {}" .format(sum,diff,prod,quotient,mod,power))


angle = 45 * math.pi / 180


print("tan(x) = {}, cos(x) = {}, sin(x) = {}" .format(math.tan(angle), math.cos(angle), math.sin(angle)))
# pip install matplotlib 

# plot graphs of sine, cosine and tangent from -360 to +360