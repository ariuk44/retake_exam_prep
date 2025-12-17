def isIsolated(n):
    if n > 2097151 or n < 1:
        return -1
    square = n * n
    cube = n * n * n
    while square > 0:
        digit_sq = square % 10
        square //= 10
        temp = cube
        while temp > 0:
            digit_cb = temp % 10
            if digit_sq == digit_cb:
                return 0
            temp //= 10
    return 1

print(isIsolated(59))

def isStacked(n):
    if n < 1:
        return 0
    total = 0
    i = 1
    while total < n:
        total += i
        if total == n:
            return 1
        i += 1
    return 0

print(isStacked(7))

def stantonMeasure(arr):
    n = 0
    count = 0
    for i in arr:
        if i == 1:
            n += 1
    for i in arr:
        if i == n:
            count += 1
    return count

print(stantonMeasure([1, 3, 1, 1, 3, 3, 2, 3, 3, 3, 4]))

def sumFactor(arr):
    if len(arr) == 0:
        return 0
    total = 0
    for i in arr:
        total += i
    count = 0
    for i in arr:
        if i == total:
            count += 1
    return count

print(sumFactor([3, 0, 2, -5, 0]))