# bmi.py
# Author: Niall O Flaherty
# This program calculates a persons BMI by calculating their weight (KG) divided by their height (CM) squared

weight = int(input('Enter Weight: '))
height = int(input('Enter Height: '))
# The above asks the user to input required information

result = int(weight / height)

print ('Your BMI is: ' + result)