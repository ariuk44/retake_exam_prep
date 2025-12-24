def isDaphne(arr):
    if len(arr) == 0:
        return 0
    has_daphne = arr[0] % 2
    for i in arr:
        if i % 2 != has_daphne:
            return 0
    return 1
print(isDaphne([3, 2, 5]))

def isDaphne1(arr):
    n = len(arr)
    if n == 0:
        return 0
    start_even = 0
    i = 0
    while i < n and arr[i] % 2 == 0:
        start_even += 1
        i += 1
    end_even = 0
    i = n - 1
    while i >= 0 and arr[i] % 2 == 0:
        end_even += 1
        i -= 1
    has_odd = 0
    for i in arr:
        if i % 2 != 0:
            has_odd = 1
            break
    return 1 if has_odd == 1 and start_even == end_even else 0
print(isDaphne1([2, 8, 7, 10, -4, 6]))

def isDigitIncreasing(n):
    for i in range(1, 10):
        total = 0
        digit = 0
        while total < n:
            digit = digit * 10 + i
            total += digit
            if total == n:
                return 1
    return 0
print(isDigitIncreasing(24))

def isDigitSum(n, m):
    if n < 0 or m < 0:
        return -1
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10
    return 1 if digit_sum < m else 0
print(isDigitSum(32121, 10))

def isDivisible(arr, divisor):
    if divisor == 0 or len(arr) == 0:
        return 0
    for x in arr:
        if x % divisor != 0:
            return 0
    return 1
print(isDivisible([6, 12, 24, 36], 12))