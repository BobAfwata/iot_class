#!/usr/bin/env python3

# This is a python code that adds two numbers in tkinter GUI
# Date - 23 Apr 2024
# Author : Gabriel Opiyo
# email : gabrielopiyo1133@gmail.com



from tkinter import *
def add_numbers():
    result = int(input_1.get()) + int(input_2.get())
    result_label.config(text = "Result: {}" .format(result))

def delete_1():
    input_1.delete(0, END)
def delete_2():
    input_2.delete(0, END)



window = Tk()
window.title("Add two numbers")
window.geometry("500x250")

num_1 = Label(window, text = "Number 1:")
num_1.place(x = 10, y = 50)
input_1 = Entry(window,  )
input_1.place(x = 70, y = 50)

num_2 = Label(window, text = "Number 2:")
num_2.place(x = 10, y = 100)
input_2 = Entry(window)
input_2.place(x = 70, y = 100)



add_button = Button(window, text = "Add", font = ("Helvetica", 10), command = add_numbers)
add_button.place(x = 100, y = 150)

delete_button_1 = Button(window, text = "Delete", font = ("Helvetica", 10), fg = "red", command = delete_1)
delete_button_1.place(x = 200, y = 50)

delete_button_2 = Button(window, text = "Delete", font = ("Helvetica", 10), fg = "red", command = delete_2)
delete_button_2.place(x =200, y = 100)

result_label = Label(window, text = "Result", font = 12)
result_label.place(x = 100, y = 200)

window.mainloop()