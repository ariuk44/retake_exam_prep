def encodeArray(n):
    result = []
    if n < 0:
        result.append(-1)
        n = -n
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    i = len(digits) - 1
    while i >= 0:
        digit = digits[i]
        count = 0
        while count < digit:
            result.append(0)
            count += 1
        result.append(1)
        i -= 1
    return result

print(encodeArray(999))

def isPrime(n):
    if n < 2:
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1

def isBunkerArray(arr):
    for i in arr:
        if i % 2 != 0 and isPrime(i) == 1:
            return 1
    return 0

print(isBunkerArray([4, 9, 6, 15, 21]))

def isFineArray(arr):
    i = 0
    while i < len(arr):
        if isPrime(arr[i]) == 1:
            found = 0
            j = 0
            while j < len(arr):
                if arr[j] == arr[i] - 2 or arr[j] == arr[i] + 2:
                    found = 1
                    break
                j += 1
            if found == 0:
                return 0
        i += 1
    return 1

print(isFineArray([3, 8, 15]))

def isMagicArray(arr):
    if len(arr) == 0:
        return 0
    total = 0
    has_prime = 0
    for i in arr:
        if isPrime(i) == 1:
            total += i
            has_prime += 1
    if has_prime == 0:
        return 1 if arr[0] == 0 else 0
    return 1 if arr[0] == total else 0

print(isMagicArray([8, 5, -5, 5, 3]))