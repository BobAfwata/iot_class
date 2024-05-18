#!/usr/bin/env python3

# This is a python code that uses the cars.py module to create a car dealership system in python
# Date - 18 Apr 2024
# Author : Gabriel Opiyo
# email : gabrielopiyo1133@gmail.com


import cars

#in each array:
#year {1}, price {2}, engine {3}, weight {4}, horsepower {5}, acceleration {6}
brand = input("Brands in stock are Toyota and Ford. Which brand are you considering? ")
if brand == "Toyota":
    print("The models available for Toyota are ", cars.model_t)
    car_type = input("Which model would you like? ")
elif brand == "Ford":
    print("The models available for Ford are ", cars.model_f)
    car_type = input("Which model would you like? ")
else:
    print("Brand not found!")

if car_type == "Corolla":
    cars.Corolla()
elif car_type == "Crown":
    cars.Crown()
elif car_type == "Vitz":
    cars.Vitz()
elif car_type == "F-150":
    cars.F_150()
elif car_type == "Focus":
    cars.Focus()
elif car_type == "Mustang":
    cars.Mustang()
else:
    print("Model not found!")






