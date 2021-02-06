# Programming & Security - Problem Sheet
## Niall O Flaherty - G00398819

# Outline
This README is used to add notes / comments regarding weeklky tasks for "Programming for CyberSecurity". Most of the info here will be duplicate of comments within each .py.

Reference for formatting: https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax

# TOPIC 02 - bmi.py - BMI Calculator
*Write a program that calculates somebody's Body Mass Index (BMI). The inputs are the person's height in centimetres and weight in kilograms. The output  is their weight divided by their height in metres squared.*

Code:
```
weight = int(input('Enter Weight in KG: '))
height = float(input('Enter Height in CM: '))
result = (weight / height / height) * 10000
print ('Your BMI is: {:.2f}'.format(result))
```

**INPUT:** I had to research to use FLOAT rather than INT when inputting height, as height is calculated in meters and to use a decimal you must use FLOAT
(int only works with whole numbers)

**PRINT:** I had to research how I could print both a text result and also the output of the calculation. This was done using {}.format which was covered in lecture videos

**PRINT:** Originally, the output produced several digits after the decimal place. Usually, BMI is produced to 2 decimal places (ie. 24.65). To reduce the output result to 2 decimal places, :.2f was placed within the curly braces.


**REFERENCES**

Stack Overflow "BMI Calculator in Python" - https://stackoverflow.com/questions/20405610/bmi-calculator-in-python/20405792#:~:text=')%20while%20input%20%3D%3D%20'imperial,which%20means%20you%20are%20underweight.

Stack Overflow "How do I let the user input a decimal number aswell as an integer?" - https://stackoverflow.com/questions/35520965/how-do-i-let-the-user-input-enter-a-decimal-number-as-well-as-just-an-integer/35521117

W3 Schools "Python String Formatting" - https://www.w3schools.com/python/python_string_formatting.asp

Slack Chat Forums - Discussion with classmates




#TOPIC 03 - bitcoin.py - Bitcoin price in US$
*Write a program that prints out todays bitcoin price in dollars.*

Code:
```

```
