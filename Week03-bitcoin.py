# Week03-bitcoin.py
# Author: Niall O Flaherty
# This Program grabs curret Bitcoin value from a .json file online and then outputs in US$
# It also outputs current Bitcoin value in 3 currencies
# NOTE: From withi VSCode, run the following command: pip install requests 
# This allows you to grab information from an external source
# REFERENCE: https://realpython.com/python-json/cls
# REFERENCE: https://www.w3schools.com/python/python_for_loops.asp
# REFERENCE: https://github.com/hanumancode/Bitcoingit -Price-Python
# REFERENCE: https://www.coindesk.com/coindesk-api

import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
# The URL of the data we are grabbing

returnedData = requests.get(url)
# This defines that the information we are grabbing is from a URL (HTTPS)

print("Todays Bitcoin price in USD\t" + returnedData.json()['bpi']['USD']['rate'])
print("Todays Bitcoin price in EUR\t" + returnedData.json()['bpi']['EUR']['rate'])
print("Todays Bitcoin price in GBP\t" + returnedData.json()['bpi']['GBP']['rate'])
# \t creates a tab which results in a tidier output