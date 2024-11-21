def Ana(s1, s2):
    count = [0] * 26
    for char in s1:
        count[ord(char) - ord('a')] += 1
    for char in s2:
        count[ord(char) - ord('a')] -= 1
    return sum(abs(x) for x in count)

s1 = input().strip()
s2 = input().strip()
print(Ana(s1, s2))
