#!/usr/bin/env python3

# This is a python code to demonstrate how to break and continue loops in python
# Date - 17 Apr 2024
# Author : Gabriel Opiyo
# email : gabrielopiyo1133@gmail.com


for i in range(0,10):
    print(i)
    if i > 6:
        i = i + 1
        break
        
    elif i == 8:
        continue

