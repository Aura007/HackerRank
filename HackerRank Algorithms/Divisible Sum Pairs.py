def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    return count

# Example usage
if __name__ == '__main__':
    n, k = map(int, input().strip().split())
    ar = list(map(int, input().strip().split()))
    result = divisibleSumPairs(n, k, ar)
    print(result)
