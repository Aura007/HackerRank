#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    
    n=len(arr)
    p=0
    q=0
    r=0
    
    for i in range(n):
        if arr[i]>0:
            p=p+1
        
        elif arr[i]<0:
            q=q+1
        
        else:
            r=r+1
    print(f"{p/n:0.6f}")
    print(f"{q/n:0.6f}")
    print(f"{r/n:0.6f}")
    
        
            
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


