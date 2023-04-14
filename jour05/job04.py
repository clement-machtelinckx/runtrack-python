
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

mess = input("entrez votre message : ")
clef = int(input("entrez votre clef : "))

def cryptage(lett, alpha, clef):
    for i in range(len(alpha)):
        if lett == " ":
            return" "
        elif alpha[i] == lett:
            return str(alpha[i+clef])
    return "?"

mess_cryp = ""

for lett in mess:
    mess_cryp += cryptage(lett, alpha, clef)

print(mess_cryp)
