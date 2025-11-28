def isRailroadTie(arr):
    n = len(arr)
    if n == 0:
        return 0
    if all(x == 0 for x in arr):
        return 0
    for i in range(n):
        if arr[i] == 0:
            if i == 0 or i == n - 1:
                return 0
            if arr[i - 1] == 0 or arr[i + 1] == 0:
                return 0
        else:
            neighbors = 0
            if i > 0 and arr[i - 1] != 0:
                neighbors += 1
            if i < n - 1 and arr[i + 1] != 0:
                neighbors += 1
            if neighbors != 1:
                return 0
    return 1

print(isRailroadTie([1, 3, 0, 3, 5, 0]))

def isRailroadTie1(arr):
    n = len(arr)
    if n == 0:
        return 0
    if all(x == 0 for x in arr):
        return 0
    for i in range(n):
        if arr[i] == 0:
            if i == 0 or i == n - 1:
                return 0
            if arr[i - 1] == 0 or arr[i + 1] == 0:
                return 0
        else:
            neighbors = 0
            if i > 0 and arr[i - 1] != 0:
                neighbors += 1
            if i < n - 1 and arr[i + 1] != 0:
                neighbors += 1
            if neighbors != 1:
                return 0
    return 1

print(isRailroadTie1([3, 3, 0, 3, 3, 0, 3, 3, 0, 3, 3]))

def isRailroadTie2(arr):
    n = len(arr)
    if n == 0:
        return 0
    if all(x == 0 for x in arr):
        return 0
    for i in range(n):
        if arr[i] == 0:
            if i == 0 or i == n - 1:
                return 0
            if arr[i - 1] == 0 or arr[i + 1] == 0:
                return 0
        else:
            neighbors = 0
            if i > 0 and arr[i - 1] != 0:
                neighbors += 1
            if i < n - 1 and arr[i + 1] != 0:
                neighbors += 1
            if neighbors != 1:
                return 0
    return 1

print(isRailroadTie2([1, 2, 0, 1, 2, 0, 1, 2]))

def isRailroadTie3(arr):
    n = len(arr)
    if n == 0:
        return 0
    if all(x == 0 for x in arr):
        return 0
    for i in range(n):
        if arr[i] == 0:
            if i == 0 or i == n - 1:
                return 0
            if arr[i - 1] == 0 or arr[i + 1] == 0:
                return 0
        else:
            neighbors = 0
            if i > 0 and arr[i - 1] != 0:
                neighbors += 1
            if i < n - 1 and arr[i + 1] != 0:
                neighbors += 1
            if neighbors != 1:
                return 0
    return 1

print(isRailroadTie3([]))

def largestAdjacentSum(arr):
    n = len(arr)
    if n < 2:
        return 0
    max_sum = arr[0] + arr[1]
    for i in range(n - 1):
        if arr[i] + arr[i + 1] > max_sum:
            max_sum = arr[i] + arr[i + 1]
    return max_sum
print(largestAdjacentSum([1,1,1,1,1,2,1,1,1]))

def checkConcatenatedSum(n, catlen):
    origin = n
    digit_sum = 0
    while n > 0:
        digit = n % 10
        rev_sum = 0
        i = 1
        while i <= catlen:
            rev_sum = rev_sum * 10 + digit
            i += 1
        digit_sum += rev_sum
        n //= 10
    return 1 if origin == digit_sum else 0

print(checkConcatenatedSum(198, 2))

def isLegalNumber(arr, base):
    for i in arr:
        if i < 0 or i >= base:
            return 0
    return 1

def convertToBase(arr, base):
    if isLegalNumber(arr, base) == 0:
        return -1
    result = 0
    for i in arr:
        result = result * base + i
    return result
print(convertToBase([1, 0, 1, 1], 2))