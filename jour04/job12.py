
L = [7, 11, 42, 39, 2]
print(L)
def triage():
    n = 0
    for _ in L:
        n += 1
        for i in range(n):
            for j in range(0, n - i - 1):
                if L[j] > L[j + 1]:
                    L[j], L[j + 1] = L[j + 1], L[j]


triage()
print(L)



