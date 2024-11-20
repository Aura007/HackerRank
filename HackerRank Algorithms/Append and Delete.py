# Read the initial string s
s = input().strip()

# Read the desired string t
t = input().strip()

# Read the number of operations k
k = int(input().strip())

# Find the length of the common prefix
common_length = 0
for i in range(min(len(s), len(t))):
    if s[i] == t[i]:
        common_length += 1
    else:
        break

# Calculate total operations needed
deletions_needed = len(s) - common_length
additions_needed = len(t) - common_length
total_operations_needed = deletions_needed + additions_needed

# Determine if it's possible to convert s to t with exactly k operations
if total_operations_needed <= k and (k - total_operations_needed) % 2 == 0 or len(s) + len(t) <= k:
    print("Yes")
else:
    print("No")
