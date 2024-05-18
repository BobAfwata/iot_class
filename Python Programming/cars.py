#!/usr/bin/env python3

# This is a python module that stores information about car models in python
# Date - 18 Apr 2024
# Author : Gabriel Opiyo
# email : gabrielopiyo1133@gmail.com






# create modules
# cars and their descriptions [model, year, etc.]
# smartphones and their model

# combine them to items.py


# learn about tkinter

# car
    #brand
        # multiple models under one brand
            # model made in different years
                # after identification of the specified model, display properties[specs]


brand = ["Toyota", "Ford"]
model_t = ["Corolla", "Crown", "Vitz"]
model_f = ["F-150", "Focus", "Mustang"]

# Toyota cars
corolla = [2002, 1000000, "1200cc", "280kg", "320hp", "0-100km/hr in 30sec"]
crown = [2017, 1900000, "2000cc", "360kg", "400hp", "0-100km/hr in 20sec"]
vitz = [2019, 8200000, "Hybrid(1200cc/1.2kWh)", "280kg", "270hp", "0-100km/hr in 22sec"]

#Ford cars
f_150 = [2022, 7500000, "4500cc", "1450kg", "620hp", "0-100km/hr in 39sec"]
focus = [2023, 3900000, "2500cc", "360kg", "420hp", "0-100km/hr in 18sec"]
mustang = [2019, 8200000, "4200cc", "500kg", "570hp", "0-100km/hr in 12sec"]

def Corolla(car_name, model_name, year_name, price_name, engine_name, weight_name, horsepower_name, acceleration_name):
    car_name.config(text = "Brand: {}" .format(brand[0]))
    model_name.config(text = "Model: {}".format(model_t[0]))
    year_name.config(text = "Year made: {}".format(corolla[0]))
    price_name.config(text = "Price: KES {}".format(corolla[1]))
    engine_name.config(text ="Engine: {}".format(corolla[2]))
    weight_name.config(text = "Weight: {}".format(corolla[3]))
    horsepower_name.config(text = "Horsepower: {}".format(corolla[4]))
    acceleration_name.config(text = "Acceleration: {}" .format(corolla[5]))

def Crown(car_name, model_name, year_name, price_name, engine_name, weight_name, horsepower_name, acceleration_name):
    car_name.config(text = "Brand: {} " .format(brand[0]))
    model_name.config(text = "Model: {} " .format(model_t[1]))
    year_name.config(text = "Year made: {} ".format(crown[0]))
    price_name.config(text = "Price: KES {}".format(crown[1]))
    engine_name.config(text ="Engine: {}".format(crown[2]))
    weight_name.config(text = "Weight: {} ".format(crown[3]))
    horsepower_name.config(text = "Horsepower: {}".format(crown[4]))
    acceleration_name.config(text ="Acceleration: {} ".format(crown[5]))

def Vitz(car_name, model_name, year_name, price_name, engine_name, weight_name, horsepower_name, acceleration_name):
    car_name.config(text = "Brand: {} ".format(brand[0]))
    model_name.config(text = "Model: {} ".format(model_t[2]))
    year_name.config(text = "Year made: {} ".format(vitz[0]))
    price_name.config(text = "Price: KES {}".format(vitz[1]))
    engine_name.config(text ="Engine: {}".format(vitz[2]))
    weight_name.config(text = "Weight: {} ".format(vitz[3]))
    horsepower_name.config(text = "Horsepower: {}".format(vitz[4]))
    acceleration_name.config(text ="Acceleration: {} ".format(vitz[5]))

def F_150(car_name, model_name, year_name, price_name, engine_name, weight_name, horsepower_name, acceleration_name):
    car_name.config(text = "Brand: {} ".format(brand[1]))
    model_name.config(text = "Model: {} ".format(model_f[0]))
    year_name.config(text = "Year made: {} ".format(f_150[0]))
    price_name.config(text = "Price: KES {}".format(f_150[1]))
    engine_name.config(text ="Engine: {}".format(f_150[2]))
    weight_name.config(text = "Weight: {} ".format(f_150[3]))
    horsepower_name.config(text = "Horsepower: {}".format(f_150[4]))
    acceleration_name.config(text = "Acceleration {}: ".format(f_150[5]))

def Focus(car_name, model_name, year_name, price_name, engine_name, weight_name, horsepower_name, acceleration_name):
    car_name.config(text = "Brand: {} ".format(brand[1]))
    model_name.config(text = "Model: {} ".format(model_f[1]))
    year_name.config(text = "Year made: {} ".format(focus[0]))
    price_name.config(text = "Price: KES {}".format(focus[1]))
    engine_name.config(text ="Engine: {}".format(focus[2]))
    weight_name.config(text = "Weight: {} ".format(focus[3]))
    horsepower_name.config(text = "Horsepower: {}".format(focus[4]))
    acceleration_name.config(text ="Acceleration: {} ".format(focus[5]))

def Mustang(car_name, model_name, year_name, price_name, engine_name, weight_name, horsepower_name, acceleration_name):
    car_name.config(text = "Brand: {} ".format(brand[1]))
    model_name.config(text = "Model: {} ".format(model_f[2]))
    year_name.config(text = "Year made: {} ".format(mustang[0]))
    price_name.config(text = "Price: KES {}".format(mustang[1]))
    engine_name.config(text ="Engine: {}".format(mustang[2]))
    weight_name.config(text = "Weight: {} ".format(mustang[3]))
    horsepower_name.config(text = "Horsepower: {}".format(mustang[4]))
    acceleration_name.config(text ="Acceleration: {} ".format(mustang[5]))