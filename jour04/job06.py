
L = ["pomme", "cerise", "orange"]
print(L)
def swap_liste():
    swap = L[-1]
    L[-1] = L[0]
    L[0] = swap
    return L

print(swap_liste())

