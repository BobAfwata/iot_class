#!/usr/bin/env python3

# This is a python code that shows classes in python
# Date - 25 Apr 2024
# Author : Gabriel Opiyo
# email : gabrielopiyo1133@gmail.com

class vehicle:
    color  = "red"
    mileage = 4500
    fuel_capacity = 2500
    year_of_manufacture = 2012

    def start_engine():
        print("Engine started")
    def stop_engine():
        print("Engine stopped")


    def set_mileage(self, mileage):
        self.mileage = mileage * 1.2
        return self.mileage
   
    def get_mileage():
        return mileage
    
class bikes:
    color = "orange"
    cost = 60000
    tire_diameter = 60
