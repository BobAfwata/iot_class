#!/usr/bin/env python3

# This is a python code to calculate the factorial of a number in python
# Date - 16 Apr 2024
# Author : Gabriel Opiyo
# email : gabrielopiyo1133@gmail.com



"""
def factorial(n):
    n_factorial = n * (n-1) * (n-2) * (n-3) * (n-4) * (n-5)
    print(n_factorial)

factorial(6)


"""

def add_numbers(num1, num2):
    sum_nums = num1 + num2
    return sum_nums

print(add_numbers(3,4))

print("\n")

def factorial(n):
    n_factorial = 1
    for i in range(0, n):
        if n == 0:
            print(n_factorial) 
        elif i == 1:
            n_factorial = n * (n-i)
        else:
            n_factorial = n_factorial * (n-i)
    if n < 0:
        print("Impossible")
    else:
        print("{}! is equal to {}" .format(n, n_factorial))
factorial(int(input("Factorial of: ")))