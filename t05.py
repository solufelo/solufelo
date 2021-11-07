"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Solomon Olufelo
ID:     210729170
Email:  oluf9170@wlu.ca
__updated__ = "2021-09-16"
------------------------------------------------------------------------
"""
from functions import range_total


start = int(input("Enter start value"))
increment = int(input("Enter increment"))
count = int(input("Enter count value"))

total = range_total(start, increment, count)
print (f"{total}")