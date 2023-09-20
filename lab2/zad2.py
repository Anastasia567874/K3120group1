def puz(s):
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] > s[j]:
                s[i], s[j] = s[j], s[i]
    return s

s = [6, 5, 4, 3, 2, 1]
s = puz(s)
print(s)