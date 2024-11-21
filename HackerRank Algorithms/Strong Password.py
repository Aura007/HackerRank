#!/bin/python3

import os

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    has_digit = False
    has_lower = False
    has_upper = False
    has_special = False
    
    for char in password:
        if char in numbers:
            has_digit = True
        elif char in lower_case:
            has_lower = True
        elif char in upper_case:
            has_upper = True
        elif char in special_characters:
            has_special = True
            
    missing_types = 0
    if not has_digit:
        missing_types += 1
    if not has_lower:
        missing_types += 1
    if not has_upper:
        missing_types += 1
    if not has_special:
        missing_types += 1
        
    additional_length_needed = max(0, 6 - n)
    
    return max(missing_types, additional_length_needed)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    password = input().strip()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')
    fptr.close()
