def isComplete(arr):
    n = len(arr)
    has_even = 0
    has_square = 0
    has_sum8 = 0
    for i in range(n):
        x = arr[i]
        if x % 2 == 0:
            has_even = 1
        if x >= 0:
            k = 0
            while k * k <= x:
                if k * k == x:
                    has_square = 1
                    break
                k += 1
        for j in range(i + 1, n):
            if arr[i] != arr[j] and arr[i] + arr[j] == 8:
                has_sum8 = 1
                break
        if has_even and has_square and has_sum8:
            return 1
    return 0

print(isComplete([3, 7, 23, 13, 107, -99, 97, 81]))

def isComplete1(arr):
    n = len(arr)
    maxEven = None
    minEven = None
    for x in arr:
        if x & 2 == 0:
            if minEven is None or x < minEven:
                minEven = x
            if maxEven is None or x > maxEven:
                maxEven = x
    if minEven is None:
        return 0
    if minEven == maxEven:
        return 0
    for v in range(minEven + 1, maxEven):
        found = 0
        for x in arr:
            if x == v:
                found = 1
                break
        if found == 0:
            return 0
    return 1

print(isComplete1([-5, 6, 2, 3, 2, 4, 5, 11, 8, 7]))

def isComplete2(arr):
    maxEven = None
    for i in arr:
        if i <= 0:
            return 0
        if i % 2 == 0:
            if maxEven is None or i > maxEven:
                maxEven = i
    if maxEven is None:
        return 0
    for v in range(2, maxEven, 2):
        found = 0
        for i in arr:
            if v == i:
                found = 1
                break
        if found == 0:
            return 0
    return 1

print(isComplete2([2, -3, 4, 3, 6]))

def isHollow(arr):
    n = len(arr)
    i = 0
    left = 0
    while i < n and arr[i] != 0:
        left += 1
        i += 1
    zero = 0
    while i < n and arr[i] == 0:
        zero += 1
        i += 1
    right = 0
    while i < n:
        if arr[i] == 0:
            return 0
        right += 1
        i += 1
    if zero >= 3 and left == right:
        return 1
    return 0

print(isHollow([8,3,0,0,0,3,3]))

def isMeera(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[j] == arr[i] * 2:
                return 0
    return 1

print(isMeera([8, 5, 4]))

def isMeera1(n):
    if n <= 1:
        return 0
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1
    if count > 0 and n % count == 0:
        return 1
    return 0

print(isMeera1(6))

def isMeera2(arr):
    n = len(arr)
    total = 0
    for i in range(n):
        if arr[i] >= i:
            return 0
        total += arr[i]
    return 1 if total == 0 else 0

print(isMeera2([-4, 0, 1, 0, 2, 1]))

def isMeera3(arr):
    has_prime = 0
    has_zero = 0
    for i in arr:
        if i == 0:
            has_zero = 1
        elif i > 1:
            prime = 1
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    prime = 0
                    break
            if prime == 1:
                has_prime = 1
    if has_prime == has_zero:
        return 1
    return 0

print(isMeera3([3, 0, 7, 6, 10, 1]))

def isBean(arr):
    n = len(arr)
    has_contain9 = False
    has_contain13 = False
    has_contain7 = False
    has_contain16 = False
    for i in range(n):
        if arr[i] == 9:
            has_contain9 = True
        if arr[i] == 7:
            has_contain7 = True
        if arr[i] == 16:
            has_contain16 = True
        if arr[i] == 13:
            has_contain13 = True
    if has_contain7 and has_contain16:
        return 0
    if has_contain9 and not has_contain13:
        return 0
    return 1

print(isBean([4, 7, 16]))

def isBean1(arr):
    n = len(arr)
    for i in range(n):
        found = 0
        for j in range(n):
            if arr[i] + 1 == arr[j] or arr[i] - 1 == arr[j]:
                found = 1
                break
        if found == 0:
            return 0
    return 1

print(isBean1([1, 1, 1, 2, 1, 1]))

def isBean2(arr):
    n = len(arr)
    for i in range(n):
        found = 0
        for j in range(n):
            if arr[i] * 2 == arr[j] or (arr[i] * 2) + 1 == arr[j] or arr[i] // 2 == arr[j]:
                found = 1
                break
        if found == 0:
            return 0
    return 1

print(isBean2([3, 8, 4]))