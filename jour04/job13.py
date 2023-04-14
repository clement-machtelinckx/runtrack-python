
L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
print(L)
def triage():
    n = 0
    for _ in L:
        n += 1
        for i in range(n):
            for j in range(0, n - i - 1):
                if L[j] > L[j + 1]:
                    L[j], L[j + 1] = L[j + 1], L[j]


def effacer():
    i = 0
    n = 0
    for _ in L:
            n += 1
    while i < n:
        j = i + 1
        m = 0
        for _ in L:
            m += 1
        while j < m:
            if L[i] == L[j]:
                del L[j]
                m -= 1
            else:
                j += 1
        i += 1


triage()
print(L)
effacer()
print(L)
