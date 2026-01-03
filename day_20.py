def isPairedN(arr, n):
    if len(arr) < 2:
        return 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == n and i + j == n:
                return 1
    return 0
print(isPairedN([8, -8, 8, 8, 7, 7, -7], 15))

def isPascal(n):
    if n < 1:
        return 0
    i = 1
    total = 0
    while total < n:
        total += i
        if total == n:
            return 1
        i += 1
    return 0
print(isPascal(6))

def isPerfectSquare(n):
    if n < 0:
        return 0
    i = 0
    while i * i <= n:
        i += 1
    return i * i
print(isPerfectSquare(5))

def isPrime(n):
    if n < 2:
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1

def isPrimeHappy(n):
    if n <= 2:
        return 0
    total = 0
    has_prime = 0
    for i in range(2, n):
        if isPrime(i) == 1:
            total += i
            has_prime =1
    if has_prime == 0:
        return 0
    return 1 if total % n == 0 else 0
print(isPrimeHappy(2))