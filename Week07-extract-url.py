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

import re
# Regex module

with open ('Week07-access.log', 'r') as file:
# 'r' denotes read-only
    for line in file:
        result = re.findall(r'(?:(get|post|head|put|delete|connect|options|trace|patch) )(\S+)', line)
# I tried searching for sentence beginning with / but was un-successful.
# The alternative was to find any possibiliy of HTTP methods, of which there are 9.
# Not case sensitive

print(result)