#!/usr/bin/env python3

# This is a python code that calculates volume/surface area of a sphere/cylinder in python
# Date - 23 Apr 2024
# Author : Gabriel Opiyo
# email : gabrielopiyo1133@gmail.com



# volume of a sphere
pi = 3.142

def calc_volsph():
    rsph = int(input("Enter radius of sphere "))
    volsph = 4/3 * pi * rsph * rsph * rsph
    print("The volume of a sphere of radius",rsph,"is",volsph)

# volume of a cylinder
def calc_volcyl():
    rcyl = int(input("Enter radius of cylinder "))
    hcyl = int(input("Enter height of cylinder "))
    volcyl = pi * rcyl * rcyl * hcyl
    print("The volume of a cylinder of radius",rcyl,"and height",hcyl,"is",volcyl)

#surface area of a sphere
def calc_surfsph():
    rsph = int(input("Enter radius of sphere "))
    surfsph = 4 * pi * rsph * rsph
    print("The surface area of a sphere of radius",rsph,"is",surfsph)


#surface area of a cylinder [closed]
def calc_surfcyl():
    rcyl = int(input("Enter radius of cylinder "))
    hcyl = int(input("Enter height of cylinder "))
    dcyl = 2 * rcyl
    surfcyl = (2 * pi * rcyl * rcyl) + pi * dcyl * hcyl
    print("The surface area of a closed cylinder of radius",rcyl,"and height",hcyl,"is",surfcyl)

    # CASE 

# specify geometrical shape [sphere/cylinder]
# specify calculation type [volume/surface area]
geotype = input("sphere/cylinder? ")

if geotype == "sphere":
    calctype = input("volume/surface area? ")
    if calctype == "volume":
        calc_volsph()
    elif calctype == "surface area":
        calc_surfsph()
    else: print("Invalid input")
else:
    if geotype == "cylinder":
        calctype = input("volume/surface area? ")
        if calctype == "volume":
            calc_volcyl()
        elif calctype == "surface area":
            calc_surfcyl()

    else: print("Invalid input")