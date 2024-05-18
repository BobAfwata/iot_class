#!/usr/bin/env python3

# This is a python code to demonstrate how functions work in python
# Date - 16 Apr 2024
# Author : Gabriel Opiyo
# email : gabrielopiyo1133@gmail.com


# functions are a block of code excuted together
# function declaration
def print_info(name, age, gender, fav_color):
    print(name)
    print(age)
    print(gender)
    print(fav_color)
    

# function call
print_info("Gabriel Opiyo", "17", "Male", "Green")
print("\n")
print_info("Michael Opondo", "19", "Male", "Blue")

max_num = int(input("Enter the maximum number: "))

def sum_numbers(max_num):
    sum = 0
    for i in range(0,max_num):
        sum = sum + i
    print(sum)


def product_numbers(max_num):
    product = 1
    for i in range(1,max_num+1):
        product = product * i
    print(product)




#sum_numbers(max_num)
product_numbers(max_num)
