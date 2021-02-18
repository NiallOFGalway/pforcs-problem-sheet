# Week04-collatz.py
# Author: Niall OFlaherty
# This program asks you to input a positive integer. 
# At each step; if the input integer is even, divide by 2; if it is un-even, multiply by 3 and add 1. Program ends if value is 1

# Reference: https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff
# Reference: Andrew Beatty e-mail query
# Reference: https://en.wikibooks.org/wiki/Python_Programming/Operators
# Reference: https://stackoverflow.com/questions/20337489/python-how-to-keep-repeating-a-program-until-a-specific-input-is-obtained

number = int(input("Enter a positive integer: "))
# Requests the user to input a positive integer

def thenumber(number):
    if number % 2 == 0:
        (print(number // 2 ))
# If the number divided by 2 does not have a remainder, it is even.
# Therefore return the even number divided by 2
    
    else:
        return (print(int(number * 3 +1)))
# Otherwise, return the number, multiply by 3 and add 1

thenumber(number)
# Execute the definition above