def fullnessQuotient(n):
    if n < 1:
        return -1
    count = 0
    for base in range(2, 10):
        temp = n
        has_zero = 0
        while temp > 0:
            digit = temp % base
            if digit == 0:
                has_zero = 1
                break
            temp //= base
        if has_zero == 0:
            count += 1
    return count
print(fullnessQuotient(94))

def allValuesTheSame(arr):
    if len(arr) == 0:
        return 0
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            return 0
    return 1
print(allValuesTheSame([432123456]))

def clusterCompression(arr):
    if len(arr) == 0:
        return []
    res = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            res.append(arr[i])
    return res
print(clusterCompression([8, 8, 6, 6, -2, -2, -2]))

def clusterCompression1(arr):
    if len(arr) == 0:
        return []
    result = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[result] = arr[i]
            result += 1
    return result
print(clusterCompression1([8, 8, 6, 6, -2, -2, -2]))

def countDigit(n, m):
    if n < 0 or m < 0:
        return -1
    if n == 0:
        return 1 if m == 0 else 0
    count = 0
    while n > 0:
        digit = n % 10
        if digit == m:
            count += 1
        n //= 10
    return count
print(countDigit(33331, 6))

def countOnes(n):
    count = 0
    while n > 0:
        if n % 2 == 1:
            count += 1
        n //= 2
    return count
print(countOnes(15))