def isZeroLimited(arr):
    for i in range(len(arr)):
        if i % 3 == 1:
            if arr[i] != 0:
                return 0
        else:
            if arr[i] == 0:
                return 0
    return 1
print(isZeroLimited([1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]))

def isZeroPlentiful(arr):
    n = len(arr)
    i = 0
    zero_seq = 0
    has_zero = 0
    while i < n:
        if arr[i] != 0:
            i += 1
        else:
            has_zero = 1
            zero_seq += 1
            count = 0
            while i < n and arr[i] == 0:
                count += 1
                i += 1
            if count < 4:
                return 0
    return zero_seq if has_zero == 1 else 0

print(isZeroPlentiful([1, 0, 0, 0, 2, 0, 0, 0, 0]))

def isSequencedArray(arr, m, n):
    if len(arr) == 0:
        return 0
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return 0
        if arr[i] < m or arr[i] > n:
            return 0
    if arr[-1] < m or arr[-1] > n:
        return 0
    for x in range(m, n + 1):
        found = 0
        for j in arr:
            if j == x:
                found = 1
        if found == 0:
            return 0
    return 1
print(isSequencedArray([1, 2, 3, 4, 5], 1, 5))

def isGuthrie(n):
    if n < 1:
        return 0
    current = 1
    step = 1
    while current < n:
        current += step
        step += 1
    return 1 if current == n else 0
print(isGuthrie(8))