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

def matches(arr, p):
    i = 0
    for seq in p:
        need = abs(seq)
        want_pos = seq > 0
        for _ in range(need):
            if i >= len(arr):
                return 0
            v = arr[i]
            if want_pos:
                if v <= 0:
                    return 0
            else:
                if v >= 0:
                    return 0
            i += 1
    return 1 if i == len(arr) else 0

print(matches([1, 2, 3, -5, -5, 2, 3, 18], [3, -2, 2, -1]))

def match_pattern(a, pattern):
    n = len(a)
    m = len(pattern)

    i = 0          # индекс into a
    k = 0          # индекс into pattern
    matches = 0    # pattern[k] хэд удаа дарааллааар таарсан бэ

    while i < n:
        if a[i] == pattern[k]:
            # одоогийн pattern[k]-тэй таарлаа
            matches += 1
            i += 1
        else:
            # таараагүй үед
            if matches == 0 or k == m - 1:
                # 1) энэ pattern[k] огт таараагүй (matches == 0)
                # 2) эсвэл бид аль хэдийн pattern-ийн сүүлчийн элемент дээр байна (k == m-1)
                return 0
            else:
                # Дараагийн pattern элемент рүү шилжинэ
                k += 1
                matches = 0
                if k >= m:
                    # pattern дууссан мөртлөө array дээр элемент үлдсэн
                    return 0
                # i-г нэмэхгүй! Одоогийн a[i]-г шинэ pattern[k]-тэй
                # дараагийн while эргэлт дээр дахин шалгана

    # массив бүрэн дууссан үед pattern-ийн сүүлчийн элемент дээр байж байх ёстой
    return 1 if i == n and k == m - 1 else 0
