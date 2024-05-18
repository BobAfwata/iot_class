#!/usr/bin/env python3

# This is a python code that plots trigonnometric graphs in matplotlib
# Date - 23 Apr 2024
# Author : Gabriel Opiyo
# email : gabrielopiyo1133@gmail.com



import numpy as np
import matplotlib.pyplot as plt
from math import pi
#plot 1[sine]
plt.subplot(1,3,1)
plt.title("Sine(-2pi<x<2pi)")
x = np.arange(-2*pi, 2*pi, 1/48*pi)
np.deg2rad(x)
y = np.sin(x)
plt.grid(True)

plt.xlabel("Angle value(*180/pi)")
plt.plot(x, y, color = "r")

#plot 2[cosine]
plt.subplot(1,3,2)
plt.title("Cosine(-2pi<x<2pi)")
x = np.arange(-2*pi, 2*pi, 1/48*pi)
np.deg2rad(x)
y = np.cos(x)
plt.grid(True)

plt.xlabel("Angle value(*180/pi)")
plt.plot(x, y, color = "g")

#plot 3[tangent]
plt.subplot(1,3,3)
plt.title("Tangent(-2pi<x<2pi)")
x = np.arange(-2*pi, 2*pi, 1/48*pi)
np.deg2rad(x)
y = np.tan(x)
plt.grid(True)

plt.xlabel("Angle value(*180/pi)")
plt.plot(x, y, color = "b")


plt.show()