def isVesuvian(n):
    count = 0
    a = 0
    while a * a < n:
        b = a
        while a * a + b * b <= n:
            if a * a + b * b == n:
                count += 1
                if count == 2:
                    return 1
            b += 1
        a += 1
    return 0
print(isVesuvian(85))

def isWave(arr):
    if len(arr) == 0:
        return 0
    for i in range(len(arr) - 1):
        if arr[i] % 2 == 0 and arr[ i + 1] % 2 == 0 or arr[i] % 2 != 0 and arr[ i + 1] % 2 != 0:
            return 0
    return 1
print(isWave([7, 2, 9, 10, 0]))

def isZeroBalanced(arr):
    if len(arr) == 0:
        return 0
    total = 0
    for i in arr:
        total += i
    if total != 0:
        return 0
    for i in arr:
        if i > 0:
            found = 0
            for j in arr:
                if j == -i:
                    found = 1
                    break
            if found == 0:
                return 0
    return 1

print(isZeroBalanced([-3, 1, 2, -2, -1, 3]))