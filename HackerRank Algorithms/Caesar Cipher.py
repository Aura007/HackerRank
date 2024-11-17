#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    k=k%26
    enc=[]
    for char in s:
        if char.isalpha():
            base=ord("A") if char.isupper() else ord('a')
            sc=chr((ord(char)-base+k)%26+base)
            enc.append(sc)
        else:
            enc.append(char)
    return ''.join(enc)
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
