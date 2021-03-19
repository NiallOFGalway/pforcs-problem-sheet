# Week07-extract-url.py
# Author: Niall O Flaherty
# This program extracts URL from a log file
# ie The part of the URL that is stored in the access.log file, complete with the query parameters (I am aware that the host name is not stored in this file, the referring host is)
# The program should store the URLs as strings in a list
# Reference: https://realpython.com/regex-python/
# Reference: https://www.w3schools.com/python/python_regex.asp
# Reference: https://cheatography.com/davechild/cheat-sheets/regular-expressions/
# Reference: Week07 Andrew Beatty Video
# Reference: https://stackoverflow.com/questions/20320719/constructing-regex-pattern-to-match-sentence/20320828
# Reference: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
# Reference: https://www.w3schools.com/python/python_file_handling.asp
# Reference: https://www.w3schools.com/python/ref_file_readlines.asp
# Reference: https://stackoverflow.com/questions/839994/extracting-a-url-in-python
# Reference: https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file

import re
# Regex module

outputFileName = "Week07-OutputFile.txt"

with open ('Week07-access.log', 'r') as file:
# 'r' denotes read-only
    for line in file:
        result = re.findall('(?:(GET|POST|HEAD|PUT|DELETE|CONNECT|OPTIONS|TRACE|PATCH) )(\S+)', line)
        print(result)
# I tried searching for sentence beginning with / but was un-successful.
# The alternative was to find any possibiliy of HTTP methods, of which there are 9.
# CASE SENSITIVE - VS Code Crl+F is *not* case sensitive, so it took a long time to realise the reason I had no output is because Python *IS* case sensitive.
# The above will output the results to screen.

'''
with open ('Week07-access.log', 'r') as file:
    with open (outputFileName, 'w') as outputFile:
        for line in file: 
            result = re.findall('(?:(GET|POST|HEAD|PUT|DELETE|CONNECT|OPTIONS|TRACE|PATCH) )(\S+)', line)
            print(result, file=open("Week07-OutputFile.txt", "a"))
'''
# The above commented code would output the results to OutputFile.txt in the same folder as the .py file
# a = attribute

