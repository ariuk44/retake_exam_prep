def isSystematicallyIncreasing(arr):
    i = 0
    expected_max = 1
    while i < len(arr):
        for value in range(1, expected_max + 1):
            if i >= len(arr) or arr[i] != value:
                return 0
            i += 1
        expected_max += 1
    return 1
print(isSystematicallyIncreasing([1, 1, 2]))

def isTriangular(n):
    if n < 1:
        return 0
    i = 1
    total = 0
    while total < n:
        total += i
        i += 1
    return 1 if total == n else 0
print(isTriangular(4))

def isTriple(arr):
    if len(arr) < 3:
        return 0
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count != 3:
            return 0
    return 1
print(isTriple([3, 1, 2, 1, 3, 1, 3, 2, 2]))

def isPrime(n):
    if n < 2:
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1

def isTwin(arr):
    if len(arr) < 2:
        return 0
    for i in range(len(arr)):
        n = arr[i]
        if isPrime(n) == 1:
            is_twin_prime = (isPrime(n - 2) == 1) or (isPrime(n + 2) == 1)
            if is_twin_prime:
                found = 0 
                for x in arr:
                    if x == n - 2 or x == n + 2:
                        if isPrime(x) == 1:
                            found = 1
                            break
                if found == 0:
                    return 0
    return 1
print(isTwin([1, 17, 8, 25, 67]))

def isTwinPrime(n):
    if n < 2:
        return 0
    if isPrime(n) == 1:
        if isPrime(n - 2) == 1 or isPrime(n + 2) == 1:
            return 1
    return 0
print(isTwinPrime(7))