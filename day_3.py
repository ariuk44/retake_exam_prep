def isRailroadTie(arr):
    n = len(arr)
    if n == 0:
        return 0
    if all(x == 0 for x in arr):
        return 0
    for i in range(n):
        if arr[i] == 0:
            if i == 0 or i == n - 1:
                return 0
            if arr[i - 1] == 0 or arr[i + 1] == 0:
                return 0
        else:
            neighbors = 0
            if i > 0 and arr[i - 1] != 0:
                neighbors += 1
            if i < n - 1 and arr[i + 1] != 0:
                neighbors += 1
            if neighbors != 1:
                return 0
    return 1

print(isRailroadTie([1, 3, 0, 3, 5, 0]))

def isRailroadTie1(arr):
    n = len(arr)
    if n == 0:
        return 0
    if all(x == 0 for x in arr):
        return 0
    for i in range(n):
        if arr[i] == 0:
            if i == 0 or i == n - 1:
                return 0
            if arr[i - 1] == 0 or arr[i + 1] == 0:
                return 0
        else:
            neighbors = 0
            if i > 0 and arr[i - 1] != 0:
                neighbors += 1
            if i < n - 1 and arr[i + 1] != 0:
                neighbors += 1
            if neighbors != 1:
                return 0
    return 1

print(isRailroadTie1([3, 3, 0, 3, 3, 0, 3, 3, 0, 3, 3]))

def isRailroadTie2(arr):
    n = len(arr)
    if n == 0:
        return 0
    if all(x == 0 for x in arr):
        return 0
    for i in range(n):
        if arr[i] == 0:
            if i == 0 or i == n - 1:
                return 0
            if arr[i - 1] == 0 or arr[i + 1] == 0:
                return 0
        else:
            neighbors = 0
            if i > 0 and arr[i - 1] != 0:
                neighbors += 1
            if i < n - 1 and arr[i + 1] != 0:
                neighbors += 1
            if neighbors != 1:
                return 0
    return 1

print(isRailroadTie2([1, 2, 0, 1, 2, 0, 1, 2]))

def isRailroadTie3(arr):
    n = len(arr)
    if n == 0:
        return 0
    if all(x == 0 for x in arr):
        return 0
    for i in range(n):
        if arr[i] == 0:
            if i == 0 or i == n - 1:
                return 0
            if arr[i - 1] == 0 or arr[i + 1] == 0:
                return 0
        else:
            neighbors = 0
            if i > 0 and arr[i - 1] != 0:
                neighbors += 1
            if i < n - 1 and arr[i + 1] != 0:
                neighbors += 1
            if neighbors != 1:
                return 0
    return 1

print(isRailroadTie3([]))