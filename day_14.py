def isConsecutiveFactored(n):
    if n <= 0:
        return 0
    for i in range(2, n // 2 + 1):
        if n % i == 0 and n % (i + 1) == 0:
            return 1
    return 0
print(isConsecutiveFactored(10))

def isContinuousFactored(n):
    if n <= 0:
        return 0
    for i in range(2, n // 2 + 1):
        product = i
        next_num = i + 1
        while product < n:
            product *= next_num
            next_num += 1
            if product == n:
                return 1
    return 0

print(isContinuousFactored(60))

def isCubePerfect(arr):
    n = len(arr)
    for i in range(n):
        has_cube = 0
        limit = abs(arr[i])
        j = -limit
        while j <= limit:
            root = j * j * j
            if root == arr[i]:
                has_cube = 1
                break
            j += 1
        if has_cube == 0:
            return 0
    return 1

print(isCubePerfect([3, 7, 21, 36]))

def isCubePowerful(n):
    if n <= 0:
        return 0
    sum_cube = 0
    original = n
    while n > 0:
        digit = n % 10
        sum_cube += digit * digit * digit
        n //= 10
    return 1 if original == sum_cube else 0

print(isCubePowerful(87))        