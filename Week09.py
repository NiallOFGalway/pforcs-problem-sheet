# Week09.py
# Author: Niall O Flaherty
'''
Find which sessionId downloaded the most data

Read the access.log into a dataframe (see lab)
Set the date time to be the index (you will need to manipulate this data, see lab)
Use regular expressions to extract the session id from the URLs and store them in a different column (use the apply function, see lab)
Use groupBy to get the sum of all the data downloaded by each sessionId.
Create a plot of this (type of your choice)
'''
# Reference:
# Reference:
# Reference:

import pandas as pd 
import re
import matplotlib.pyplot as plot

# File to read data from
filename = "Week09-access.log"

