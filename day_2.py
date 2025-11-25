def countRepresentations(numRupees):
    coins = [1, 2, 5, 10, 20]
    dp = [0] * (numRupees + 1)
    dp[0] = 1
    for c in coins:
        for amount in range(c, numRupees + 1):
            dp[amount] += dp[amount - c]
    return dp[numRupees]

print(countRepresentations(12))

def countRepresentations1(numPurees):
    coins = [1, 2, 5, 10, 20]
    dp = [0] * (numPurees + 1)
    dp[0] = 1
    for c in coins:
        for amount in range(c, numPurees + 1):
            dp[amount] += dp[amount - c]
    return dp[numPurees]

print(countRepresentations1(12))

def countRepresentations2(numPurees):
    coins = [1, 2, 5, 10, 20]
    dp = [0] * (numPurees + 1)
    dp[0] = 1
    for c in coins:
        for x in range(c, numPurees + 1):
            dp[x] += dp[x - c]
    return dp[numPurees]

print(countRepresentations2(6))

def countRepresentations3(numRupees):
    coins = [1, 2, 5, 10, 20]
    dp = [0] * (numRupees + 1)
    dp[0] = 1
    for c in coins:
        for x in range(c, numRupees + 1):
            dp[x] += dp[x - c]
    return dp[numRupees]

print(countRepresentations3(12))

def minCoins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for c in coins:
        for x in range(c, amount + 1):
            dp[x] = min(dp[x], dp[x - c] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

print(minCoins([1, 2, 5], 11))

def isPerfectSquare(n):
    if n < 0:
        return False
    i = 1
    while i * i <= n:
        if i * i == n:
            return True
        i += 1
    return False

def countSquarePairs(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            x = arr[i]
            y = arr[j]
            if x > 0 and y > 0 and isPerfectSquare(x + y):
                count += 1
    return count

print(countSquarePairs([11, 5, 4, 20, 11]))

def countSquarePairs1(arr):
    cnt = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            x = arr[i]
            y = arr[j]
            if x > 0 and y > 0 and isPerfectSquare(x + y):
                cnt += 1
    return cnt

print(countSquarePairs1([9, 0, 2, -5, 7]))

def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

def solve10(n):
    fact10 = factorial(n)
    for x in range(1, n + 1):
        for y in range(x, n + 1):
            if factorial(x) + factorial(y) == fact10:
                return [x, y]
    return [0, 0]

print(solve10(10))

def filterArray(arr, n):
    if n < 0:
        return None
    result = []
    index = 0
    while n > 0:
        if n % 2 == 1:
            if index >= len(arr):
                return None
            result.append(arr[index])
        n //= 2
        index += 1
    return result

print(filterArray([8, 4, 9, 0, 3, 1, 2], 88))

def filterArray1(arr, n):
    if n < 0:
        return 0
    result = []
    index = 0
    while n > 0:
        if n % 2 == 1:
            if index >= len(arr):
                return None
            result.append(arr[index])
        n //= 2
        index += 1
    return result

print(filterArray1([0, 9, 12, 18, -6], 11))