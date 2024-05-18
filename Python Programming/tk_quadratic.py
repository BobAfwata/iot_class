#!/usr/bin/env python3

# This is a python code that solves quadratic equations in tkinter GUI
# Date - 23 Apr 2024
# Author : Gabriel Opiyo
# email : gabrielopiyo1133@gmail.com



from tkinter import *
import math

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

def quadratic():
    a = int(a_value.get())
    b = int(b_value.get())
    c = int(c_value.get())
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / 2*a
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / 2*a
    
    x1_label.config(text = "x1 = {}" .format(x1))
    x2_label.config(text = "x2 = {}" .format(x2))

window = Tk()
window.title("Quadratic Equations Calculator")
window.geometry("500x500")

title_1 = Label(window, text = "ax^2 + bx + c = 0")
title_1.pack()

a_label = Label(window, text = "a =")
a_label.place(x = 10, y = 50)

b_label = Label(window, text = "b =")
b_label.place(x = 10, y = 75)

c_label = Label(window, text = "c =")
c_label.place(x = 10, y = 100)


a_value = Entry(window)
a_value.place(x = 30, y = 50)

b_value = Entry(window)
b_value.place(x = 30, y = 75)

c_value = Entry(window)
c_value.place(x = 30, y = 100)


result_button = Button(window, text = "Result", command = quadratic)
result_button.place(x = 30, y = 120)

x1_label = Label(window, text = "x1 =")
x1_label.place(x = 10, y = 150)

x2_label = Label(window, text = "x2 =")
x2_label.place(x = 10, y = 170)

window.mainloop()