# Programming & Security - Problem Sheet
## Niall O Flaherty - G00398819

# Outline
This README is used to add notes / comments relating to weeklky tasks for "Programming for CyberSecurity". Most of the info here will be duplicate of comments within
each .py. While some may consider this README to contain too much information, as a beginner to Python I am purposely over-commenting for my own benefit for 
future reference

Reference for formatting: https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax

# WEEK 02 - bmi.py - BMI Calculator
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




# WEEK 03 - bitcoin.py - Bitcoin price in US$
*Write a program that prints out todays bitcoin price in dollars.*

Install Requests - Execute the below code within VS Code Terminal to allow requests
```
pip install requests
```

Code:
```
import requests
url = "https://api.coindesk.com/v1/bpi/currentprice.json"

returnedData = requests.get(url)

print("Todays Bitcoin price in USD\t" + returnedData.json()['bpi']['USD']['rate'])
print("Todays Bitcoin price in EUR\t" + returnedData.json()['bpi']['EUR']['rate'])
print("Todays Bitcoin price in GBP\t" + returnedData.json()['bpi']['GBP']['rate'])
```
It took quite some time by trial-and-error to learn what I actually needed to pull from the .json to provide me with the data I wanted. I knew that the currency abbreviations and the rate were was the key data, but I kept getting errors when I executed the .py. After searching online (see references below), I noted that one user included the 'bpi' field (Bitcoin Price Index). I was un-sure as to why including this field was crucial, however after adding it, the output was correct.

**REFERENCES**

"Working With JSON Data in Python" - https://realpython.com/python-json/

"Python Project for Beginners: Bitcoin Price Notifications" - https://realpython.com/python-bitcoin-ifttt/

"Python for Loops" - https://www.w3schools.com/python/python_for_loops.asp

"Bitcoin Price Python" - https://github.com/hanumancode/Bitcoin-Price-Python

API - https://www.coindesk.com/coindesk-api




# WEEK 04 - collatz.py - Bitcoin price in US$
*Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.
At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
Have the program end if the current value is 1.*

Code:
```
while True:
    try:
        integer = int(input("Please enter a positive number: "))
  
    except ValueError:
        print ("Hey, that's not a number! Please try again: ")
        continue

    else: 
        if integer <1:
            print("You entered either 0, or a negative number. Please try again: ")
            continue
        break

def number(integer):
    if integer % 2 == 0:
        return (integer / 2)  
    else: 
        return ((integer * 3) + 1)    

if integer > 0:
    while integer != 1:
        print(integer)
        integer = number(integer)
```

1) We need to define the integer, however there are rules
    - The input must be a number
    - The integer must be greater than 0
    * If these rules are not met, the user must try again

2) Now that we have passed the rules, we must check
    - If the integer is even (when devided by 2, the remainder is 0), return the integer divided by 2
    - If the integer is odd, multiply the integer by 3 and add 1

3) If the integer is greater than 0 and while it is greater than 1, print the values

**REFERENCES**

https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff

Andrew Beatty e-mail query

https://en.wikibooks.org/wiki/Python_Programming/Operators

https://stackoverflow.com/questions/20337489/python-how-to-keep-repeating-a-program-until-a-specific-input-is-obtained

https://www.w3schools.com/python/python_try_except.asp

https://www.w3schools.com/python/python_while_loops.asp

https://www.w3schools.com/python/python_functions.asp




# Week 05 - squareroot.py - Get the Square Root of a number using Newton Method
*Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. Do not use built-in function math.sqrt(x) - Instead use Newton Method. You should create a function called <tt>sqrt</tt> that does this.*

Code:
```
def squareRoot(number, number_iters = 1000000):
    numberToBeRooted = (float(number))
  
    for i in range (number_iters):
        number = 0.5 * (number + numberToBeRooted / number)
    
    return number

inputNumber = float(input("Please enter a positive number: "))

sqrt = (squareRoot(inputNumber))

print("The Square Root of {} is approx. {}".format(inputNumber,sqrt))
```

1) Define the function using def
2) Calculate the Square Root using Newton Method (As found in References
3) Return the number
4) Call the function
5) Print the final result

**REFERENCES**

https://www.geeksforgeeks.org/python-math-function-sqrt/#:~:text=sqrt()%20function%20is%20an,number%20passed%20in%20the%20parameter.

https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d

https://www.youtube.com/watch?v=2GrfaB88w4M

https://www.youtube.com/watch?v=nDlip0Mg8tE



# Week 06 - Week06-CountEs.py
*Write a program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line.*

Code:
```
filetocount = str(input("Enter TXT file to count (include extension .txt): "))


with open (filetocount, 'r') as file:
   
    read = file.read()

    count = read.count('e')

    print(count)
```

1) Asks the user to input the filename (include .txt extension)
2) Open the file (NOTE: 'r' means read-only)
- NOTE: There is an older method to open file (f = open) it was advised not to use this as you must close the file (f.close()) after. Failing to do so could mean other users may not be able to close the file.
3) Read the File
4) Count the number of 'e' in the file
5) Print the result

**REFERENCES**

https://stackoverflow.com/questions/30876497/open-a-file-from-user-input-in-python-2-7

https://pythonexamples.org/python-count-number-of-words-in-text-file/

Andrew Beatty Week06 Lecture Video

https://pythonexamples.org/python-count-number-of-characters-in-text-file/
