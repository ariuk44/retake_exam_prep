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

def fullnessQuotient(n):
    if n < 1:
        return -1
    count = 0
    for base in range(2, 10):
        temp = n
        has_zero = False
        while temp > 0:
            digit = temp % base
            temp //= base
            if digit == 0 and temp > 0:
                has_zero = True
                break
        if not has_zero:
            count += 1
    return count

print(fullnessQuotient(94))

def isIsolated(n: int) -> int:
    if n < 1 or n > 2097151:
        return -1

    square = n * n
    cube = n * n * n

    while square > 0:
        digit_sq = square % 10
        square //= 10

        temp = cube
        while temp > 0:
            digit_cb = temp % 10
            temp //= 10
            if digit_sq == digit_cb:
                return 0
    return 1

print(isIsolated(169))