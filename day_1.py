def isInertial(arr):
    if len(arr) < 2:
        return 0
    max_val = max(arr)
    if max_val % 2 != 0:
        return 0
    even_vals = [i for i in arr if i % 2 == 0 and i != max_val]
    odd_vals = [i for i in arr if i % 2 != 0]
    if not odd_vals:
        return 0
    for odd in odd_vals:
        for even in even_vals:
            if even > odd:
                return 0
    return 1

print(isInertial([2, 12, 12, 4, 6, 8, 11]))

def isMadhavArray(arr):
    n = len(arr)
    k = 1
    total_len = 1
    while total_len < n:
        k += 1
        total_len += k
    if total_len != n:
        return 0
    target = arr[0]
    idx = 1
    group_size = 2
    while idx < n:
        if sum(arr[idx: idx + group_size]) != target:
            return 0
        idx += group_size
        group_size += 1
    return 1

print(isMadhavArray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, -2, -1]))

def isMadhavArray1(arr):
    n = len(arr)
    k = 1
    total = 1
    while total < n:
        k += 1
        total += k
    if total != n:
        return 0
    target = arr[0]
    idx = 1
    group_size = 2
    while idx < n:
        if sum(arr[idx: idx + group_size]) != target:
            return 0
        idx += group_size
        group_size += 1
    return 1

print(isMadhavArray1([18, 9, 10, 6, 6, 6]))

def isMadhavArray2(arr):
    n = len(arr)
    k = 1
    total = 1
    while total < n:
        k += 1
        total += k
    if total != n:
        return 0
    target = arr[0]
    idx = 1
    group_size = 2
    while idx < n:
        if sum(arr[idx: idx + group_size]) != target:
            return 0
        idx += group_size
        group_size += 1
    return 1

print(isMadhavArray2([6, 2, 4, 2, 2, 2, 1, 5, 0, 0]))

def isNUnique(arr, n):
    if len(arr) < 2:
        return 0
    cnt = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == n:
                cnt += 1
                if cnt > 1:
                    return 0
    return 1 if cnt == 1 else 0

print(isNUnique([7, 3, 3, 2, 4], 11))

def isNUnique1(arr, n):
    if len(arr) < 2:
        return 0
    cnt = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == n:
                cnt += 1
                if cnt > 1:
                    return 0
    return 1 if cnt == 1 else 0

print(isNUnique1([7, 3, 3, 2, 4], 4))

def isNUnique2(arr, n):
    if len(arr) < 2:
        return 0
    cnt = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == n:
                cnt += 1
                if cnt > 1:
                    return 0
    return 1 if cnt == 1 else 0

print(isNUnique2([1], 2))

def isOddHeavy(arr):
    even_vals = []
    odd_vals = []
    for i in arr:
        if i % 2 == 0:
            even_vals.append(i)
        else:
            odd_vals.append(i)
    if not odd_vals:
        return 0
    if even_vals and max(even_vals) > min(odd_vals):
        return 0
    return 1

print(isOddHeavy([2, 4, 6, 8, 11]))

def isOddHeavy1(arr):
    even_vals = [i for i in arr if i % 2 == 0]
    odd_vals = [i for i in arr if i % 2 != 0]
    if not odd_vals:
        return 0
    if not even_vals:
        return 1
    return 1 if even_vals and max(even_vals) < min(odd_vals) else 0

print(isOddHeavy1([-1]))