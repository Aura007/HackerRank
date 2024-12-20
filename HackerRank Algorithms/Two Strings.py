#!/bin/python3

import os

def twoStrings(s1, s2):
    # Convert both strings to sets to find common characters
    set1 = set(s1)
    set2 = set(s2)
    
    # Check for intersection
    if set1.intersection(set2):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()
        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
