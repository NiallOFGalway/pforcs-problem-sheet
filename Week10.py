# Week10.py
'''
Write a (bullet proof) function called averageTo(aList, toIndex)
The function should take in a list and an index. 
The function will return the average of the numbers upto and including the toIndex in the aList.
When I say "bullet proof", I would like the function to always return an integer, even if a error occurs (say return -1), but it will use logging to make a meaningful log warning, for any error that occurs (eg the aList contains an entry that is not a number/ toIndex is not valid, there are many things that could go wrong)
Write the code to test all the things that could go wrong with this function, and a test to check the function does work.
The test code can be in the same file or different file.
'''
# Author: Niall OFlaherty

# Reference: https://stackoverflow.com/questions/4288973/whats-the-difference-between-s-and-d-in-python-string-formatting#:~:text=The%20%25d%20is%20for%20numbers,and%20%25s%20is%20for%20strings.&text=you%20can%20assign%20those%20variables,a%20tuple%20of%20the%20variables.&text=They%20are%20used%20when%20you,with%20a%20specific%20format%20enforced.
# Reference: https://realpython.com/python-logging/
# Reference: Andrew Beatty Week 10 Lab


import logging
logging.basicConfig(level=logging.DEBUG)
# Enables logging. 5 options: Debug, Info, Warning, Error, Critical 





