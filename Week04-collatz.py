# Week04-collatz.py
# Author: Niall OFlaherty
# This program asks you to input a positive integer. 
# At each step; if the input integer is even, divide by 2; if it is un-even, multiply by 3 and add 1. Program ends if value is 1

# Reference: https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff
# Reference: Andrew Beatty e-mail query
# Reference: https://en.wikibooks.org/wiki/Python_Programming/Operators
# Reference: https://stackoverflow.com/questions/20337489/python-how-to-keep-repeating-a-program-until-a-specific-input-is-obtained
# Reference: https://www.w3schools.com/python/python_try_except.asp
# Reference: https://www.w3schools.com/python/python_while_loops.asp
# Reference: https://www.w3schools.com/python/python_functions.asp

while True:
    try:
        integer = int(input("Please enter a positive number: "))
# Asks the user to input a positive number. (try)
  
    except ValueError:
        print ("Hey, that's not a number! Please try again: ")
        continue
# Checks that the value inputted is indeed an integer (int). Once ths is true, it will continue.

    else: 
        if integer <1:
            print("You entered either 0, or a negative number. Please try again: ")
            continue
        break
# Checks that the value inptted is greater than 0. Once this is true, it will continue and then breaks (break), to stop a loop.

def number(integer):
    if integer % 2 == 0:
        return (integer / 2)  
    else: 
        return ((integer * 3) + 1)
# This defines what we want the output to be. If the number is even (divided by 2, no remainder, hence even), return the number divided by 2
# Otherwise, multiple the integer by 3 and add 1      

if integer > 0:
    while integer != 1:
        print(integer)
        integer = number(integer)
# If the integer is greater than 0, print the output.
# Only do this while (while) the integer is not equal to 1. 
