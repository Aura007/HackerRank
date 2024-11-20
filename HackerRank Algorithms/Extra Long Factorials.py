def extraLongFactorials(n):
    # Initialize result to 1 (the factorial of 0 is 1)
    res = 1
    
    # Calculate factorial iteratively
    for i in range(1, n + 1):
        res *= i
    
    # Print the result
    print(res)

if __name__ == '__main__':
    n = int(input().strip())
    extraLongFactorials(n)
