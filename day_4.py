def repsEqual(arr, n):
    i = 0
    while i < len(arr) and arr[i] == 0:
        i += 1
    num = 0
    while i < len(arr):
        num = num * 10 + arr[i]
        i += 1
    return 1 if num == n else 0

print(repsEqual([0, 0, 0,3, 2, 0, 5, 3], 32053))

def isCentered15(arr):
    n = len(arr)
    total = 0
    for i in range(n):
        for j in range(i + 1, n):
            total = sum(arr[i:j + 1])
            if total == 15:
                left = i
                right = n - j - 1
                if right == left:
                    return 1
    return 0

print(isCentered15([3, 2 , 10, 4, 1, 6, 9]))