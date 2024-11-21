def Palin(s):
    from collections import Counter
    count = Counter(s)
    odd_count = sum(1 for freq in count.values() if freq % 2 != 0)
    
    if odd_count > 1:
        return "NO"
    else:
        return "YES"


s = input().strip()
print(Palin(s))
