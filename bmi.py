# bmi.py
# Author: Niall O Flaherty
# This program calculates a persons BMI by calculating their weight (KG) divided by their height (CM) squared
# Reference: https://stackoverflow.com/questions/20405610/bmi-calculator-in-python/20405792#:~:text=')%20while%20input%20%3D%3D%20'imperial,which%20means%20you%20are%20underweight.
# Reference: https://stackoverflow.com/questions/35520965/how-do-i-let-the-user-input-enter-a-decimal-number-as-well-as-just-an-integer/35521117

weight = int(input('Enter Weight in KG: '))
height = float(input('Enter Height in Meters: '))
# The above asks the user to input required information
# float must be used for height as we are working in meters hence require the use of decimals, otherwise only a whole number would be accepted.

result = weight/(height*height)

print ('Your BMI is: {}'.format(result))
## This took quite a bit of de-bugging as I had to figure out how to be able to add both text and the result to the same line
# Before I tried {}.format I was getting errors