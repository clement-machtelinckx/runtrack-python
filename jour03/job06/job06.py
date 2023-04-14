alpha = "abcdefghijklmnopqrstuvwxyz"*10
i=1
while i <=len(alpha):
    print(alpha[:i])
    alpha=alpha[i:]
    i+=1


