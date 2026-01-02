def isLayered(arr):
    if len(arr) < 2:
        return 0
    count = 1
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return 0
        if arr[i] == arr[i - 1]:
            count += 1
        else:
            if count < 2:
                return 0
            count = 1
    if count < 2:
        return 0
    return 1

print(isLayered([1, 2, 2, 2, 3, 3]))

def isMartian(arr):
    count1 = 0
    count2 = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count1 += 1
        if arr[i] == 2:
            count2 += 1
        if i > 0 and arr[i] == arr[i-1]:
            return 0
    return 1 if count1 > count2 else 0

print(isMartian([1, 2, 1, 2, 1, 2, 1, 2, 1]))

def isMercurial(arr):
    seen_one = 0
    seen_three = 0
    for i in arr:
        if i == 1:
            if seen_three == 1:
                return 0
            seen_one = 1
        elif i == 3 and seen_one:
            seen_three = 1
    return 1
print(isMercurial([3, 2, 18, 1, 0, 3, -11, 1, 3]))

def isPrime(n):
    if n < 2:
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1

def isNPrimeable(arr, n):
    for i in arr:
        if isPrime(i + n) == 0:
            return 0
    return 1
print(isNPrimeable([5, 15, 27], 2))