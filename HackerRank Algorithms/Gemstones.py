#!/bin/python3

import os
from collections import Counter

def gemstones(arr):
    mineral_counts = Counter(arr[0])
    for rock in arr[1:]:
        mineral_counts &= Counter(rock)
    return len(mineral_counts)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')
    fptr.close()
