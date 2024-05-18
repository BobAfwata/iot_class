from cars import * 
from tkinter import *
from tkinter import ttk

def choose_brand():
    brand = var.get()
    var.set(None)
    if brand == "Toyota":
        brand_name.config(text = "The selected brand is {}" .format(brand))
        model_types.config(text = "The models available for Toyota are {}" .format(model_t))
        car_type = Label(
            root,
            text = "Which model would you like?",
        )
        car_type.place(x = 20, y = 150)

        global car
        car = Entry(
            root,
        )
        car.place(x = 180, y = 150)

        submit = Button(
            root,
            text = "Submit",
            command = car_info
        )
        submit.place(x = 100, y = 170)
    elif brand == "Ford":
        brand_name.config(text = "The selected brand is {}" .format(brand))
        model_types.config(text = "The models available for Ford are {}" .format(model_f))
        car_type = Label(
            root,
            text = "Which model would you like?",
        )
        car_type.place(x = 20, y = 150)

        car = Entry(
            root,
        )
        car.place(x = 180, y = 150)
        submit = Button(
            root,
            text = "Submit",
            command = car_info
        )
        submit.place(x = 100, y = 170)
    else:
        pass

def car_info():
    car_type = car.get()
    if car_type == "Corolla":
        Corolla(car_name, model_name, year_name, price_name, engine_name, weight_name, horsepower_name, acceleration_name)
    elif car_type == "Crown":
        Crown(car_name, model_name, year_name, price_name, engine_name, weight_name, horsepower_name, acceleration_name)
    elif car_type == "Vitz":
        Vitz(car_name, model_name, year_name, price_name, engine_name, weight_name, horsepower_name, acceleration_name)
    elif car_type == "F-150":
        F_150(car_name, model_name, year_name, price_name, engine_name, weight_name, horsepower_name, acceleration_name)
    elif car_type == "Focus":
        Focus(car_name, model_name, year_name, price_name, engine_name, weight_name, horsepower_name, acceleration_name)
    elif car_type == "Mustang":
        Mustang(car_name, model_name, year_name, price_name, engine_name, weight_name, horsepower_name, acceleration_name)
    else:
        pass

root = Tk()
root.title("Car Information")
root.geometry("650x650")
brand = Label(
    root,
    text = "Brands in stock are Toyota and Ford. Which brand are you considering?",
)
brand.place(x = 10, y = 10)

var = StringVar()

toyota = ttk.Radiobutton(
    root,
    text = "Toyota",
    variable = var,
    value = "Toyota",
    
)
toyota.place(x= 20, y = 40)

ford = ttk.Radiobutton(
    root,
    text = "Ford",
    variable = var,
    value = "Ford",
)
ford.place(x= 120, y = 40)

confirm = Button(
    root,
    text = "Confirm",
    command = choose_brand,
)
confirm.place(x = 70, y = 70)

brand_name = Label(
    root,
    text = "",
)
brand_name.place(x = 20, y = 95)

model_types = Label(
    root,
    text = ""
)
model_types.place(x = 20, y = 120)

car_name = Label(
    root,
    text = ""
)
car_name.place(x = 40, y = 200)

model_name = Label(
    root,
    text = ""
)
model_name.place(x = 40, y = 225)

year_name = Label(
    root,
    text = ""
)
year_name.place(x = 40, y = 250)

price_name = Label(
    root,
    text = ""
)
price_name.place(x = 40, y = 275)

engine_name = Label(
    root,
    text = ""
)
engine_name.place(x = 40, y = 300)

weight_name = Label(
    root,
    text = ""
)
weight_name.place(x = 40, y = 325)

horsepower_name = Label(
    root,
    text = ""
)
horsepower_name.place(x = 40, y = 350)

acceleration_name = Label(
    root,
    text = ""
)
acceleration_name.place(x = 40, y = 375)

root.mainloop()