def is121Array(arr):
    n = len(arr)
    if n == 0:
        return 0
    i = 0
    count1_start = 0
    while i < n and arr[i] == 1:
        count1_start += 1
        i += 1
    if count1_start == 0:
        return 0
    count2 = 0
    while i < n and arr[i] == 2:
        count2 += 1
        i += 1
    if count2 == 0:
        return 0
    count1_end = 0
    while i < n and arr[i] == 1:
        count1_end += 1
        i += 1
    if i != n:
        return 0
    return 1 if count1_end == count1_start else 0
print(is121Array([1, 1, 2, 2, 2, 1, 1, 1]))

def is235Array(arr):
    count2 = 0
    count3 = 0
    count5 = 0
    countOther = 0
    for i in arr:
        if i % 2 == 0:
            count2 += 1
        if i % 3 == 0:
            count3 += 1
        if i % 5 == 0:
            count5 += 1
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
            countOther += 1
    return 1 if (count2 + count3 + count5 + countOther) == len(arr) else 0
print(is235Array([3, 9, 27, 7, 1, 1, 1, 1, 1]))

def largestDifferenceOfEvens(arr):
    max_even = None
    min_even = None
    count_even = 0
    for i in arr:
        if i % 2 == 0:
            count_even += 1
            if max_even is None or i > max_even:
                max_even = i
            if min_even is None or i < min_even:
                min_even = i
    if count_even < 2:
        return -1
    return max_even - min_even
print(largestDifferenceOfEvens([1, 18, 5, 7, 33]))

def isPrime(n):
    if n < 2:
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1

def largestPrimeFactor(n):
    if n <= 1:
        return 0
    max_prime = 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            if isPrime(i) == 1 and i > max_prime:
                max_prime = i
            other = n // i
            if isPrime(other) == 1 and other > max_prime:
                max_prime = other
        i += 1
    if isPrime(n) == 1:
        return n
    return max_prime
print(largestPrimeFactor(6936))

def minDistance(n):
    if n <= 1:
        return 0
    prev = 0
    min_dist = n
    for i in range(1, n + 1):
        if n % i == 0:
            if prev != 0:
                dist = i - prev
                if dist < min_dist:
                    min_dist = dist
            prev = i
    return min_dist
print(minDistance(13013))