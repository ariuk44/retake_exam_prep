def minDistance(n):
    if n < 1:
        return -1
    factors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n//i)
        i += 1
    factors.sort()
    if len(factors) < 2:
        return 0
    min_diff = factors[1] - factors[0]
    for i in range(1, len(factors) - 1):
        diff = factors[i + 1] - factors[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff

print(minDistance(63))