#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    weights = set()  # To store unique weights
    current_char = ''
    current_weight = 0
    
    # Calculate weights for uniform substrings
    for char in s:
        if char == current_char:
            # If the same character, increase its cumulative weight
            current_weight += (ord(char) - ord('a') + 1)
        else:
            # If a new character, reset current_weight
            current_char = char
            current_weight = ord(char) - ord('a') + 1
        
        # Add the current weight to the set
        weights.add(current_weight)
    
    # Prepare results for each query
    results = []
    for query in queries:
        if query in weights:
            results.append("Yes")
        else:
            results.append("No")
    
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input().strip()  # Read input string

    queries_count = int(input().strip())  # Read number of queries

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)  # Call the function

    fptr.write('\n'.join(result))  # Write results to output file
    fptr.write('\n')

    fptr.close()  # Close the file
