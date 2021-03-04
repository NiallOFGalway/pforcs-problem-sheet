# Week06-CountEs.py
# Author: Niall O Flaherty
# Write a program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line.
# Reference: https://stackoverflow.com/questions/30876497/open-a-file-from-user-input-in-python-2-7
# Reference: Andrew Beatty Week06 Lecture Video
# Reference: https://pythonexamples.org/python-count-number-of-words-in-text-file/
# Reference: https://pythonexamples.org/python-count-number-of-characters-in-text-file/
# Reference: https://www.geeksforgeeks.org/python-string-count/


filetocount = str(input("Enter TXT file to count (include extension .txt): "))
# Asks user to enter file in which to count.

with open (filetocount, 'r') as file:
# Opens the file the user has input NOTE: 'r' means read-only    
    read = file.read()
# Read the data in the txt file
    count = read.count('e')
# Count the numbers of 'e' in the txt file
    print(count)
# Print the result