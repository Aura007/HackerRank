# Read the number of test cases
t = int(input().strip())

# Loop through each test case
for _ in range(t):
    # Read the integer n for this test case
    n = int(input().strip())
    
    # Initialize a counter for divisible digits
    count = 0
    
    # Convert n to a string to iterate over each digit
    for d in str(n):
        # Check if the digit is not '0' and if it divides n evenly
        if d != '0' and n % int(d) == 0:
            count += 1  # Increment the counter if conditions are met
    
    # Print the total count of divisible digits
    print(count)
