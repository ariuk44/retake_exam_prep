def isNice(arr):
    if len(arr) == 0:
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
print(isNice([2, 2, 3, 3, 3]))

def isPrime(n):
    if n < 2:
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1

def isNice1(arr):
    if len(arr) == 0:
        return 0
    sum_prime = 0
    for i in range(len(arr)):
        if isPrime(arr[i]) == 1:
            sum_prime += arr[i]
    return 1 if sum_prime == arr[0] else 0

print(isNice1([8, 5, -5, 5, 3]))

def isNormal(n):
    if n <= 0:
        return 0
    for i in range(3, n, 2):
        if i != n and n % i == 0:
            return 0
    return 1
print(isNormal(8))

def isOddValent(arr):
    if len(arr) < 2:
        return 0
    has_duplicate = 0
    has_odd = 0
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            has_odd = 1
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                has_duplicate = 1
    return 1 if has_odd == 1 and has_duplicate == 1 else 0
print(isOddValent([2, 2, 2, 4, 4]))

def isOneBalanced(arr):
    n = len(arr)
    if n == 0:
        return 1
    i = 0
    start_ones = 0
    while i < n and arr[i] == 1:
        start_ones += 1
        i += 1
    non_ones = 0
    while i < n and arr[i] != 1:
        non_ones += 1
        i += 1
    end_ones = 0
    while i < n and arr[i] == 1:
        end_ones += 1
        i += 1
    if i != n:
        return 0
    return 1 if start_ones + end_ones == non_ones else 0
print(isOneBalanced([1, 1, 1, 2, 3, -18, 45, 1]))

def minDistance(n):
    if n <= 1:
        return 0

    prev_factor = 0
    min_dist = n

    for i in range(1, n + 1):
        if n % i == 0:
            if prev_factor != 0:
                dist = i - prev_factor
                if dist < min_dist:
                    min_dist = dist
            prev_factor = i

    return min_dist

print(minDistance(15))