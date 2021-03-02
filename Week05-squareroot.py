# Week05-squareroot.py
# Author: Niall O Flaherty
# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
# You should create a function called <tt>sqrt</tt> that does this.
# NOTE: There is a built-in function in Python math.sqrt(x) but we were asked not to use this, therefore refer to Newton Method
# Reference: https://www.geeksforgeeks.org/python-math-function-sqrt/#:~:text=sqrt()%20function%20is%20an,number%20passed%20in%20the%20parameter.
# Reference: https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d
# Reference: https://www.youtube.com/watch?v=2GrfaB88w4M
# Reference: https://www.youtube.com/watch?v=nDlip0Mg8tE

def squareRoot(number, number_iters = 1000000):
    numberToBeRooted = (float(number))
# This is the number we want to get the SqRoot of    
    for i in range (number_iters):
        number = 0.5 * (number + numberToBeRooted / number)
# This is the manual method of getting SqRoot of a number, rather than using built-in function    
    return number

inputNumber = float(input("Enter number you wish to be square rooted: "))
# Asks the user to input a number

SRoot = (squareRoot(inputNumber))
# Calling the function

print(SRoot)
# Printing the result