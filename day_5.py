def matches(arr, p):
    i = 0
    for x in p:
        n = abs(x)
        pos = x > 0
        for _ in range(n):
            if i >= len(arr):
                return 0
            b = arr[i]
            if pos:
                if b <= 0:
                    return 0
            else:
                if b >= 0:
                    return 0
            i += 1
    return 1 if i == len(arr) else 0

print(matches([1, 2, 3, -5, -5, 2, 3, 8, 18], [3, -2, 3]))

def matches1(arr,  p):
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

print(matches1([1, 2, 3, -5, -5, 2, 3, 8], [3, -2, 3]))

def matches_pattern(arr, pattern):
    i = 0  # A дээр алхах pointer
    n = len(arr)
    m = len(pattern)

    for j in range(m):  # pattern-ийн элемент бүр дээр гүйлгэнэ
        matches_count = 0

        # дотор loop: одоогийн pattern[j]-тэй хэд дараалан таарч байгааг тоолно
        for k in range(i, n):
            if arr[k] == pattern[j]:
                matches_count += 1
            else:
                break  # энэ бүлгийн төгсгөл

        if matches_count == 0:
            return 0  # энэ pattern элемент A дотор огт эхлээгүй бол буруу

        i += matches_count  # дараагийн шалгалтыг A-гийн шинэ байрнаас эхлүүлнэ

    # pattern бүрэн таарч дууссаны дараа A ч яг дууссан байх ёстой
    return 1 if i == n else 0

print(matches_pattern([1, 1, 1, 2, 2, 1, 1, 3], [1, 2, 1, 3]))

def matches_pattern1(arr, pattern):
    i = 0
    n = len(arr)
    m = len(pattern)
    for j in range(m):
        matches_count = 0
        for k in range(i, n):
            if arr[k] == pattern[j]:
                matches_count += 1
            else:
                break
        if matches_count == 0:
            return 0
        i += matches_count
    return 1 if n == i else 0

print(matches_pattern1([1, 1, 1, 2, 2, 1, 1, 3], [1, 2, 1]))