L = [52, 38, 75, 84, 36, 24, 62, 99, 52, 37, 66]
print(L)

def note_arondi(L):
    for i in range(len(L)):
        if L[i] == (L[i] % 5):
            pass
        elif (L[i] % 5) < 3:
            pass
        elif ((L[i]) % 5) >= 3:
            (L[i]) = (L[i] + (5 - L[i] % 5))
            # print(L[i])


note_arondi(L)

print(L)