def isDual(arr):
    n = len(arr)
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
        if count != 2:
            return 0
    return 1
print(isDual([1, 2, 1, 3, 3]))

def isDual1(arr):
    n = len(arr)
    if n == 0:
        return 1
    if n % 2 != 0:
        return 0
    first_pair = arr[0] + arr[1]
    i = 2
    while i < n:
        if arr[i] + arr[i + 1] != first_pair:
            return 0
        i += 2
    return 1
print(isDual1([1, 2, 2, 1, 3, 0]))

def isEvens(n):
    if n < 0:
        return 0
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            return 0
        n //= 10
    return 1
print(isEvens(2436))

def isPrime(n):
    if n < 2:
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1

def isFactorialPrime(n):
    if n <= 1:
        return 0
    fact = 1
    k = 1
    while fact + 1 <= n:
        if fact + 1 == n:
            return isPrime(n)
        k += 1
        fact *= k
    return 0

print(isFactorialPrime(7))

def isFancy(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    prev1 = 1
    prev2 = 1
    while True:
        current = 3 * prev1 + 2 * prev2
        if current == n:
            return 1
        if current > n:
            return 0
        prev2 = prev1
        prev1 = current
print(isFancy(61))