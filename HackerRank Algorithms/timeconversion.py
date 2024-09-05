
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hr = int(s[:2])
    minu = s[3:5]
    sec = s[6:8]
    period = s[8:10]
    
    if period == "AM":
        if hr == 12:
            hr = 0
    elif period=="PM":
        if hr != 12:
            hr += 12
    return f"{hr:02}:{minu}:{sec}"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
