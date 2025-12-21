def decodeArray(arr):
    n = len(arr)
    if n < 2:
        return 0
    number = 0
    for i in range(n - 1):
        digit = abs(arr[i] - arr[i + 1])
        number = number * 10 + digit
    if arr[0] < 0:
        number = -number
    return number

print(decodeArray([2, -3, -2, 6, 9, 18]))

def decodeArray1(arr):
    if len(arr) == 0:
        return 0
    i = 0
    sign = 1
    if arr[0] == -1:
        sign = -1
        i = 1
    number = 0
    count = 0
    while i < len(arr):
        if arr[i] == 0:
            count += 1
        else:
            number = number * 10 + count
            count = 0
        i += 1
    return sign * number

print(decodeArray1([0, 1, 1, 1, 1, 1, 0, 1]))

def isAllPossibilities(arr):
    n = len(arr)
    if n == 0:
        return 0
    for i in range(n):
        found = 0
        for j in range(n):
            if arr[j] == i:
                found = 1
                break
        if found == 0:
            return 0
    return 1

print(isAllPossibilities([0, 2, 3]))

def isBalanced(arr):
    n = len(arr)
    for i in range(n):
        found = 0
        for j in range(n):
            if arr[j] == -arr[i]:
                found = 1
                break
        if found == 0:
            return 0
    return 1

print(isBalanced([-5, 2, -2]))

def isBalanced1(arr):
    n = len(arr)
    for i in range(n):
        if i % 2 == 0 and arr[i] % 2 != 0:
            return 0
        if i % 2 != 0 and arr[i] % 2 == 0:
            return 0
    return 1

print(isBalanced1([16, 6, 2, 3]))

def isBeanArray(arr):
    if len(arr) == 0:
        return 0
    sum_prime = 0
    has_prime = 0
    for i in arr:
        if i > 1:
            is_prime = 1
            for x in range(2, int(i * 0.5) + 1):
                if i % x == 0:
                    is_prime = 0
                    break
            if is_prime == 1:
                sum_prime += i
                has_prime = 1
    if has_prime == 0:
        return 1 if arr[0] == 0 else 0
    return 1 if sum_prime == arr[0] else 0

print(isBeanArray([8, 5, -5, 5, 3]))