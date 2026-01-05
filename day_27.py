def counSixes(n):
    count = 0
    while n > 0:
        if n % 10 == 6:
            count += 1
        n //= 10
    return count

def findSmallestBEQnumber():
    n = 1
    while True:
        cube = n * n * n
        if counSixes(cube) == 4:
            return n
        n += 1
print(findSmallestBEQnumber())

def goodSpread(arr):
    n = len(arr)
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
                if count > 3:
                    return 0
    return 1
print(goodSpread([2, 1, 2, 5, 2, 1, 5, 9, 9, 9, 9]))

def hasKSmallFactors(k, n):
    if n <= 0 or k <= 0:
        return False
    for i in range(1, n + 1):
        if n % i == 0:
            u = i
            v = n // i
            if u < k and v < k:
                return True
    return False
print(hasKSmallFactors(6, 30))

def hasNValues(arr, n):
    if len(arr) < n:
        return 0
    count = 0
    for i in range(len(arr)):
        found = 0
        for j in range(i):
            if arr[i] == arr[j]:
                found = 1
                break
        if found == 0:
            count += 1
    print(count)
    return 1 if count == n else 0
print(hasNValues([1, 2, 2, 1], 2))