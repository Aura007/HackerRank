def theLoveLetterMystery(s):
    left = 0
    right = len(s) - 1
    operations = 0
    
    while left < right:
        # Calculate the number of changes needed to make s[left] and s[right] equal
        operations += abs(ord(s[left]) - ord(s[right]))
        left += 1
        right -= 1
    
    return operations

# Example usage
if __name__ == '__main__':
    q = int(input().strip())
    for _ in range(q):
        s = input().strip()
        result = theLoveLetterMystery(s)
        print(result)
