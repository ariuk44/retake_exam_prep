def isSquare(n):
    if n < 0:
        return 0
    i = 0
    while i * i <= n:
        if i * i == n:
            return 1
        i += 1
    return 0

print(isSquare(1))

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primeCount(start, end):
    count = 0
    for i in range(start, end + 1):
        if isPrime(i):
            count += 1
    return count

print(primeCount(-10, 6))

def guthrieIndex(n):
    if n <= 1:
        return 0
    count = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        count += 1
    return count

print(guthrieIndex(4))

def isGuthrieSequence(arr):
    if len(arr) == 0 or arr[-1] != 1:
        return 0
    for i in range(len(arr) - 1):
        curr_index = arr[i]
        nxt_index = arr[i + 1]
        if curr_index % 2 == 0:
            expected = curr_index // 2
        else:
            expected = curr_index * 3 + 1
        if nxt_index != expected:
            return 0
    return 1

print(isGuthrieSequence([8, 17, 4, 1]))

   