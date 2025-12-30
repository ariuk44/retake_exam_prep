def isFibonacci(n):
    if n <= 0:
        return 1
    if n == 1:
        return 1
    a = 1
    b = 1
    while b < n:
        c = a + b
        a = b
        b = c
    return 1 if b == n else 0
print(isFibonacci(13))

def isFilter(arr):
    has_9 = 0
    has_11 = 0
    has_7 = 0
    has_13 = 0
    for i in arr:
        if i == 9:
            has_9 = 1
        if i == 11:
            has_11 = 1
        if i == 7:
            has_7 = 1
        if i == 13:
            has_13 = 1
    if has_9 == 1 and has_11 == 0:
        return 0
    if has_7 == 1 and has_13 == 1:
        return 0
    return 1
    
print(isFilter([9, 6, 18]))

def isHodder(n):
    if n <= 1:
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    x = n + 1
    while x % 2 == 0:
        x //= 2
    return 1 if x == 1 else 0
print(isHodder(31))

def isIntertial(arr):
    if len(arr) == 0:
        return 0
    max_val = arr[0]
    has_odd = 0
    for i in arr:
        if i >= max_val:
            max_val = i
        if i % 2 != 0:
            has_odd = 1
    if has_odd == 0:
        return 0
    if max_val % 2 != 0:
        return 0
    for x in arr:
        if x % 2 == 0 and max_val != x:
            for y in arr:
                if y % 2 != 0 and y <= x:
                    return 0
    return 1

print(isIntertial([12, 11, 4, 9, 2, 3, 10]))