#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    mini=0
    maxi=0
    minscore=scores[0]
    maxscore=scores[0]
    for score in scores[1:]:
        if score>maxscore:
            maxscore=score
            maxi+=1
    
        elif score<minscore:
            minscore=score
            mini+=1

    return [maxi,mini]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
