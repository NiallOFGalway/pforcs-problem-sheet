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
# Reference: Andrew Beatty Week09 Lab
# Reference: https://www.tutorialspoint.com/python_pandas/python_pandas_groupby.htm
# Reference: https://realpython.com/pandas-groupby/
# Reference: https://dzone.com/articles/types-of-matplotlib-in-python#:~:text=Python%20provides%20different%20types%20of,plot%20for%20viewing%20the%20data.
# Reference: Week 08 Task

import pandas as pd 
import re
import matplotlib.pyplot as plt

# File to read data from
filename = "Week09-access.log"

# Add column names (Credit: Andrew Beatty Week09 Lab)
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

# Reads the file into a dataframe (Credit: Andrew Beatty Week09 Lab)
df = pd.read_csv(filename, sep=' ', header= None, names=colNames)

# Remove the dashes from the output (Credit: Andrew Beatty Week09 Lab)
df.drop(columns=['dash1', 'dash2'], inplace=True)

# Removes [] from 'time' - I didn't realise this step had to be done so got errors when trying to change the type of column of 'time' from object to dateTime. (Credit: Andrew Beatty Week09 Lab)
df['time'] = df['time'].apply(lambda x: re.search('[\w:/]+', x).group())

# Change the type of the time column to dateTime (Current type is object) (Credit: Andrew Beatty Week09 Lab)
df['time'] = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')

# print(df) - Test
# print(df.dtypes) - Test

# Set the 'time' column to be the index
df = df.set_index(['time'])

# Regular Expression to extract the SessionId. Store in a new column
def extract_sessionid(x):
    wibble = re.search('(JSESSIONID=\S+)', x).group()
    id = re.split('=', wibble)[1]
    return id

# groupBy to get the sum of all the data downloaded by each sessionId.
df['SESSIONID'] = df['request'].apply(extract_sessionid)

print(df.groupby(by=['SESSIONID'])['size of response'].sum())

# Create a plot - Despite creating a basic plot in the previous task, this confused me a little. I resorted to seeking help from a fellow class-mate, however the outcome is that I now understand what's going on
plt.figure(figsize=(8, 8))

plotdata = df.groupby(by=['SESSIONID'])[['size of response']].sum()
plotdata['size of response'].plot(kind='bar')

# Set the plot labels
plt.title("Data downloaded by SessionID")
plt.xlabel("SSESSIONID")
plt.ylabel("Data downloaded (bytes)")

# Show the graph
plt.show()