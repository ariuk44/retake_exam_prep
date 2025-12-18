def isSequentiallyBounded(arr):
    if len(arr) == 0:
        return 0
    i = 0
    n = len(arr)
    while i < n:
        valeu = arr[i]
        if valeu <= 0:
            return 0
        count = 0
        while i < n and arr[i] == valeu:
            count += 1
            i += 1
        if count >= valeu:
            return 0
        if i < n and arr[i] < valeu:
            return 0
    return 1

print(isSequentiallyBounded([2, 3, 3, 4]))

def isSumSafe(arr):
    total = 0
    for i in arr:
        total += i
    for i in arr:
        if i == total:
            return 0
    return 1

print(isSumSafe([5, -5, 1]))

def isTrivalent(arr):
    if len(arr) < 3:
        return 0
    v1 = arr[0]
    v2 = None
    v3 = None
    for i in arr:
        if i == v1 or i == v2 or i == v3:
            continue
        elif v2 is None:
            v2 = i
        elif v3 is None:
            v3 = i
        else:
            return 0
    if v2 is not None and v3 is not None:
        return 1
    return 0

print(isTrivalent([2, 2, 3, 3, 3, 3, 2, 41]))

def isTrivalent1(arr):
    if len(arr) < 3:
        return 0
    i = 0
    count = 0
    while i < len(arr):
        j = 0
        found = 0
        while j < i:
            if arr[j] == arr[i]:
                found = 1
                break
            j += 1
        if found == 0:
            count += 1
            if count > 3:
                return 0
        i += 1
    return 1 if count == 3 else 0

print(isTrivalent1([2, 2, 3, 3, 3, 3, 2, 41, 21]))

def isVanilla(arr):
    if len(arr) == 0:
        return 1
    first_digit = abs(arr[0]) % 10
    for i in arr:
        n = abs(i)
        while n > 0:
            if n % 10 != first_digit:
                return 0
            n //= 10
    return 1

print(isVanilla([9, 999, 99999, -9999]))