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

https://www.geeksforgeeks.org/python-string-count/




# WEEK07 - Week07-extract-url.py
*Write a program called extract-url.py, that will extract the URLs from an access.log file. ie The part of the URL that is stored in the access.log file, complete with the query parameters*

Code:
```
import re

outputFileName = "Week07-OutputFile.txt"

with open ('Week07-access.log', 'r') as file** REFERENCE
    for line in file:
        result = re.findall('(?:(GET|POST|HEAD|PUT|DELETE|CONNECT|OPTIONS|TRACE|PATCH) )(\S+)', line)
        print(result)

'''
with open ('Week07-access.log', 'r') as file:
    with open (outputFileName, 'w') as outputFile:
        for line in file: 
            result = re.findall('(?:(GET|POST|HEAD|PUT|DELETE|CONNECT|OPTIONS|TRACE|PATCH) )(\S+)', line)
            print(result, file=open("Week07-OutputFile.txt", "a"))
'''
```

1) Import re imports Regex (Regular Expressions)
2) In the event of outputting the result to a separate file, define this by defining: outputFileName - NOTE: In the above code, the option to output the result is commented out. The above code outputs the result to screen
3) Open the file (In the example above, 'Week07-access.log') - Note: 'r' denotes read-only
4) Use re.findall (including your chosen pattern) - re.findall module is used to search for “all” occurrences that match a given pattern
5) Print the result

**NOTES**
- This was an incredibly tricky task. Not that there was a huge amount of code, but from researching online, it appears that there were multiple ways to produce the same result. In the end, sticking with lecture notes / lab / video proved to be the most apropriate. Following the KISS analogy; "Keep it simple, stupid".
- Once the correct regex pattern was found (which took some time), it worked perfect in VS Code, but when applied to .py and executed, the result was empty. This caused a LOT of head scratching. Eventually, the light-bulb lit and I realised that VS Code is not case sensitive, but Python is! (When I changed the get|post|head... to GET|POST|HEAD... it suddenly worked!
- According to: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods - There are 9 HTTP request methods. In the log file provided, only 2 were used (GET & POST), however, as that cannot be taken for granted, it felt safer to include all 9 request methods in the search pattern.

**REFERENCES**

https://realpython.com/regex-python/

https://www.w3schools.com/python/python_regex.asp

https://cheatography.com/davechild/cheat-sheets/regular-expressions/

Week07 Andrew Beatty Video

https://stackoverflow.com/questions/20320719/constructing-regex-pattern-to-match-sentence/20320828

https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

https://www.w3schools.com/python/python_file_handling.asp

https://www.w3schools.com/python/ref_file_readlines.asp

https://stackoverflow.com/questions/839994/extracting-a-url-in-python

https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file

# WEEK08 - Week08-plottask.py
*Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.*

Code:
```
import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(0,4))

fy = xpoints
gy = xpoints * xpoints
hy = xpoints * xpoints * xpoints

plt.plot(fy, linestyle='solid', linewidth='3', color='blue', label='fy')
plt.plot(gy, linestyle='solid', linewidth='3', color='green', label='gy')
plt.plot(hy, linestyle='solid', linewidth='3', color='red', label='hy')

plt.legend()
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()

'''
plt.savefig('Week08-PlotImage.png')
# The above code would save the output as a .png file
'''
```

1) Import Libraries
- Numpy: "NumPy is a Python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices"
- Matplotlib.pyplot: "A collection of functions that make matplotlib work like MATLAB. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc."
2) Define X (0,4)
3) Define Y Values
4) Plot the X / Y Values
5) For easier reading, a line-style, line-width, colour and label are added
6) Finally, show the plot on-screen

**NOTE**

In the Code above, there is a commented out section. If this code was used, the output would be a .png file rather then showing on-screen

**REFERENCES**

https://www.w3schools.com/python/matplotlib_pyplot.asp

https://realpython.com/python-matplotlib-guide

https://realpython.com/courses/python-histograms/

Andrew Beatty Week 08 Tutorial

https://matplotlib.org/2.0.2/users/pyplot_tutorial.html

https://stackoverflow.com/questions/16992038/inline-labels-in-matplotlib

# WEEK 09 - Week09.py
*Find which SessionID downloaded the most data and plot same*

Code:
```
import pandas as pd 
import re
import matplotlib.pyplot as plt

filename = "Week09-access.log"

colNames = ('ip',
            'dash1',
            'dash2',
            'time',
            'request',
            'status code',
            'size of response',
            'referer',
            'user agent',
            'dunno'
            )

df = pd.read_csv(filename, sep=' ', header= None, names=colNames)

df.drop(columns=['dash1', 'dash2'], inplace=True)

df['time'] = df['time'].apply(lambda x: re.search('[\w:/]+', x).group())

df['time'] = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')

df = df.set_index(['time'])

def extract_sessionid(x):
    wibble = re.search('(JSESSIONID=\S+)', x).group()
    id = re.split('=', wibble)[1]
    return id

df['SESSIONID'] = df['request'].apply(extract_sessionid)

print(df.groupby(by=['SESSIONID'])['size of response'].sum())

plt.figure(figsize=(8, 8))
plotdata = df.groupby(by=['SESSIONID'])[['size of response']].sum()
plotdata['size of response'].plot(kind='bar')
plt.title("Data downloaded by SessionID")
plt.xlabel("SSESSIONID")
plt.ylabel("Data downloaded (bytes)")
plt.show()
```

1) Import Pandas / Import MatPlotLib
2) Select file to read from
3) Add column names
4) Read the file into a dataframe
5) Remove useless data (dashes) from the dataframe
6) Remove [] from time to make it readable
7) Change the type of the time column from object to dateTime
8) Set 'time' column to be the index
9) Use groupBy to get the sum of all the data downloaded by each SESSIONID
10) Create a plot

**REFERENCES**

Andrew Beatty Week09 Lab

https://www.tutorialspoint.com/python_pandas/python_pandas_groupby.htm

https://realpython.com/pandas-groupby/

https://dzone.com/articles/types-of-matplotlib-in-python#:~:text=Python%20provides%20different%20types%20of,plot%20for%20viewing%20the%20data.

Week 08 Task
