def isValid(s):
    from collections import Counter
    
    freq = Counter(s)
    freq_counts = Counter(freq.values())
    
    if len(freq_counts) == 1:
        return "YES"
    
    if len(freq_counts) == 2:
        (f1, c1), (f2, c2) = freq_counts.items()
        return "YES" if (c1 == 1 and (f1 == f2 + 1 or f1 == 1)) or (c2 == 1 and (f2 == f1 + 1 or f2 == 1)) else "NO"
    
    return "NO"

# Example usage
if __name__ == '__main__':
    print(isValid(input().strip()))
