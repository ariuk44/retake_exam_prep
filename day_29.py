def pairwiseSum(arr):
    if arr is None or len(arr) == 0:
        return None
    if len(arr) % 2 != 0:
        return None
    result = []
    for i in range(0, len(arr), 2):
        result.append(arr[i] + arr[i + 1])
    return result
print(pairwiseSum([2, 1, 18, -5, -5, -15, 0, 0, 1, -1]))
def countFactors(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2

def sameNumberOfFactors(n1, n2):
    if n1 < 0 or n2 < 0:
        return -1
    return 1 if countFactors(n1) == countFactors(n2) else 0
print(sameNumberOfFactors(23, 97))

def sumDigits(n):
    total = 0
    temp = abs(n)
    while temp > 0:
        digit = temp % 10
        total += digit
        temp //= 10
    return total
print(sumDigits(-6543))

def sumIsPower(arr):
    if len(arr) == 0:
        return False
    total = 0
    for i in arr:
        total += i
    power = 1
    while power < total:
        power *= 2
    return power == total
print(sumIsPower([8, 8, 8, 8]))

def updateMileage(arr, miles):
    while miles > 0:
        i = 0
        arr[i] += 1
        while i < len(arr) and arr[i] == 10:
            arr[i] = 0
            i += 1
            if i < len(arr):
                arr[i] += 1
        miles -= 1
    return arr
print(updateMileage([8, 9, 9, 5, 0], 1))