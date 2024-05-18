#!/usr/bin/env python3

# This is a python code that demonstrates the while loop and uses it to calculate the factorial of a number in python
# Date - 23 Apr 2024
# Author : Gabriel Opiyo
# email : gabrielopiyo1133@gmail.com




x = 5 # is the initial value
while x < 10: # is the condition
    print(x)
    x += 2 # is the increment factor


# Assignment: use while loop to get sum of first 100 odd numbers
    # use while to get factorial of numbers
print("\n")

def factorial(n):
    
    if n > 0:
        i = 1
    else:
        i = 0
        n_factorial = 1
    
    
    while i == 1:
        n_factorial = n * (n-i)
        i += 1
    while i < n:
        n_factorial = n_factorial * (n-i)
        i += 1
    

    if n < 0:
        print("Impossible")
    else:
        print("{}! is equal to {}" .format(n, n_factorial))

factorial(int(input("Factorial of: ")))

print("\n")


def sum_odd(max_value):
    init = 1
    result = 0
    while init < max_value:
        result = result + init
        init += 2
    print(result)

sum_odd(int(input("Sum of odd numbers from 1 to: ")))