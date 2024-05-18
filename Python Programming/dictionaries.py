#!/usr/bin/env python3

# This is a python code to demonstrate dictionaries in python
# Date - 23 Apr 2024
# Author : Gabriel Opiyo
# email : gabrielopiyo1133@gmail.com


sensor_data = {
    "temp" : 12.6,
    "humidity" : 123,
    "light" : 36,
    "distance" : 60,
    "gas_level" : 20.9
}

print(sensor_data["humidity"])
sensor_data["gas_level"] = 51.7
print(sensor_data["gas_level"])
sensor_data["time_seconds"] = 42
print(sensor_data)
del(sensor_data["light"])
print(sensor_data)

for s in sensor_data.keys():
    print("The value of {} is {}" .format(s, sensor_data[s]))
print("-----------------------------------------------------")
for s in sorted(sensor_data.keys()):
    print("The value of {} is {}" .format(s, sensor_data[s]))

data = sensor_data.copy()
print(data)

def increase_humidity(sensor_data):
    new_humidity = sensor_data["humidity"] + 10
    return new_humidity

h = increase_humidity(sensor_data)

print(h)