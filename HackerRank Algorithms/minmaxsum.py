
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sum1=sum(arr)
    maxi=max(arr) 
    mini=min(arr)  
    
    print(sum1-maxi,sum1-mini)
 
        
             

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
