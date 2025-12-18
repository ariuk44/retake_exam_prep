def isMinMaxDisjoint(arr):
    max_val = arr[0]
    min_val = arr[0]
    for x in range(len(arr) - 1):
        if max_val < arr[x]:
            max_val = arr[x]
        if min_val > arr[x]:
            min_val = arr[x]
    if max_val == min_val:
        return 0
    max_count = 0
    min_count = 0
    min_index = -1
    max_index = -1
    i = 0
    while i < len(arr):
        if arr[i] == min_val:
            min_count += 1
            min_index = i
        if arr[i] == max_val:
            max_count += 1
            max_index = i
        i += 1
    if max_count != 1 or min_count != 1:
        return 0
    if abs(min_index - max_index) == 1:
        return 0
    
    return 1

print(isMinMaxDisjoint([5, 4, 1, 3, 2]))

def isPrime(n):
    if n < 2:
        return 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1

def isNiceArray(arr):
    if len(arr) == 0:
        return 0
    total = 0
    i = 0
    while i < len(arr):
        if isPrime(arr[i]) == 1:
            total += arr[i]
        i += 1
    if arr[0] == 0:
        return 1 if total == 0 else 0
    return 1 if arr[0] == total else 0

print(isNiceArray([8, 5, -5, 5, 3]))

def isOnionArray(arr):
    n = len(arr)
    for j in range(n // 2 + n % 2):
        k = n - 1 - j
        if j == k:
            continue
        if arr[j] + arr[k] > 10:
            return 0
    return 1

print(isOnionArray([-2, 5, 0, 5, 12]))

def isPacked(arr):
    i = 0
    n_len = len(arr)
    while i < n_len:
        n = arr[i]
        if n <= 0:
            return 0
        count = 0
        j = i
        while j < n_len and arr[j] == n:
            count += 1
            j += 1
        if n != count:
            return 0
        k = 0
        while k < i:
            if arr[k] == arr[i]:
                return 0
            k += 1
        i = j
    return 1

print(isPacked([4, 4, 4, 4, 1, 2, 2, 3, 3, 3]))