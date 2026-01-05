def encodeNumber(n):
    if n <= 1:
        return None
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors
print(encodeNumber(6936))

def encodeNumber1(n):
    if n <= 1:
        return None
    result = []
    for d in range(2, n + 1):
        while n % d == 0:
            result.append(d)
            n //= d
        if n == 1:
            break
    return result
print(encodeNumber1(6936))

def eval(x, arr):
    result = 0.0
    n = len(arr) - 1
    for i in range(len(arr)):
        result += arr[i] * (x ** (n - i))
    return result
print(eval(1, [0, 1, 2, 3, 4]))

def factorEqual(n, m):
    countn = 0
    countm = 0
    i = 1
    j = 1
    while i <= n:
        if n % i == 0:
            countn += 1
        i += 1
    while j <= m:
        if m % j == 0:
            countm += 1
        j += 1
    return 1 if countm == countn else 0
print(factorEqual(10, 9))

def factorCount(x):
    count = 0
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            if i * i == x:
                count += 1
            else:
                count += 2
    return count

def factorEqual1(n, m):
    return 1 if factorCount(n) == factorCount(m) else 0
print(factorEqual1(10, 33))

def factorTwoCount(n):
    if n <= 0:
        return 0
    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2
    return count
print(factorTwoCount(48)) 