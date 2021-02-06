# Programming & Security - Problem Sheet
## Niall O Flaherty - G00398819

# Outline
This README is used to add notes / comments regarding weeklky tasks for "Programming for CyberSecurity"
Most of the info here will be duplicate of comments within each .py

# WEEK02 - bmi.py - BMI Calculator
*Write a program that calculates somebody's Body Mass Index (BMI). The inputs are the person's height in centimetres and weight in kilograms. The output  is their weight divided by their height in metres squared.*

Code:
```
weight = int(input('Enter Weight in KG: '))
height = float(input('Enter Height in CM: '))
result = (weight / height / height) * 10000
print ('Your BMI is: {:.2f}'.format(result))
```

Regarding inputs, I had to research to use FLOAT rather than INT when inputting height, as height is calculated in meters and to use a decimal you must use FLOAT
(int only works with whole numbers)
Regarding the print of result, I had to research how I could print both a text result and also the output of the calculation.
This was done using {}.format which was covered in lecture videos
Reference URL's pasted within bmi.py
