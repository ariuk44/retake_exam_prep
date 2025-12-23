def isBunker(arr):
    has_one = 0
    has_prime = 0
    for i in arr:
        if i == 1:
            has_one = 1
        elif i > 1:
            prime = 1
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    prime = 0
                    break
            if prime == 1:
                has_prime = 1
    if has_one == has_prime:
        return 1
    return 0

print(isBunker([6, 10, 1]))

def isBunker1(n):
    if n < 1:
        return 0
    k = 1
    current = 1
    while current < n:
        current = current + k
        k += 1
    if current == n:
        return 1
    return 0

print(isBunker1(11))

def isCentered(arr):
    n = len(arr)
    if n % 2 == 0 or n == 0:
        return 0
    mid = n // 2
    mid_value = arr[mid]
    for i in range(n):
        if i != mid and arr[i] <= mid_value:
            return 0
    return 1

print(isCentered([3, 2, 1, 4, 5]))

def isCentered15(arr):
    n = len(arr)
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += arr[j]
            if total == 15:
                left = i
                right = n -j - 1
                if left == right:
                    return 1
            if total > 15:
                break
    return 0

print(isCentered15([1, 1, 15 -1,-1]))

def isConsectiveFactored(n):
    if n <= 0:
        return 0
    for i in range(2, n // 2 + 1):
        if n % i == 0 and n % (i + 1) == 0:
            return 1
    return 0

print(isConsectiveFactored(90))

def isConsectiveFactoredwhile(n):
    if n <= 0:
        return 0
    i = 2
    while i < n // 2:
        if n % i == 0 and n % (i + 1) == 0:
            return 1
        i += 1
    return 0

print(isConsectiveFactoredwhile(15))