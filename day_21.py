def isPrime(n):
    if n < 2:
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1

def isPrimeProduct(n):
    if n <= 1:
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            j = n // i
            if isPrime(i) == 1 and isPrime(j) == 1:
                return 1
    return 0
print(isPrimeProduct(22))

def isSetEqual(arr1, arr2):
    if len(arr1) == 0 and len(arr2) == 0:
        return 1
    for i in arr1:
        found = 0
        for j in arr2:
            if i == j:
                found = 1
        if found == 0:
            return 0
    for i in arr2:
        found = 0
        for j in arr1:
            if i == j:
                found = 1
        if found == 0:
            return 0
    return 1
print(isSetEqual([1, 9, 12], [12, 9, 12, 1, 1, 1]))

def isSmart(n):
    if n < 1:
        return 0
    current = 1
    k = 2
    while current < n:
        current += k - 1
        k += 1
    return 1 if current == n else 0
print(isSmart(8))

def isSuff(arr):
    if len(arr) < 2:
        return 0
    for i in range(len(arr)):
        found = 0
        for j in range(len(arr)):
            if arr[j] == arr[i] + 1 or arr[j] == arr[i] - 1:
                 found = 1
                 break
        if found == 0:
            return 0
    return 1
print(isSuff([3, 4, 5, 7]))