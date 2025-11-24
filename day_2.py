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