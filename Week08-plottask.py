# Week08-plottask.py
# Author: Niall O Flaherty
# Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(0,4))
# Creating the X-Axis 0,4

fy = xpoints
gy = xpoints * xpoints
hy = xpoints * xpoints * xpoints
# Creating the Y-Axis

plt.plot(fy, linestyle='solid', linewidth='3', color='blue', label='fy')
plt.plot(gy, linestyle='solid', linewidth='3', color='green', label='gy')
plt.plot(hy, linestyle='solid', linewidth='3', color='red', label='hy')
# Creates the f, g, y plot; the line-style; the line width; the colour; label 
# Advised of extra marks for making the plot look nice, did not know how far to go with this!
# plt.legend is required for the 'label' to show' (see below)

plt.legend()
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
# Legend shows the names of the lines
# plt.xlabel & plt.ylabel labels the X / Y Axis

plt.show()
# Outputs the plot on-screen

'''
plt.savefig('Week08-PlotImage.png')
# The above code would save the output as a .png file
'''