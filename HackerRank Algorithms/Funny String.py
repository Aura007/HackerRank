#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Create the reversed version of the string
    n = s[::-1]
    
    # Calculate absolute differences for the original string
    org= [abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1)]
    
    # Calculate absolute differences for the reversed string
    diff = [abs(ord(n[i]) - ord(n[i + 1])) for i in range(len(n) - 1)]
    
    # Compare both lists of differences
    if org == diff:
        return "Funny"
    else:
        return "Not Funny"

if __name__ == '__main__':
    q = int(input().strip())  # Read number of queries

    for _ in range(q):
        s = input().strip()  # Read each string
        result = funnyString(s)  # Call the function
        print(result)  # Print the result
