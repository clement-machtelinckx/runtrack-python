
# Boucle principale de 2 à 1000
for num in range(2, 1001):
    # Si le nombre est divisible par un nombre autre que 1 et lui-même
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        # Si le nombre n'est divisible que par 1 et lui-même, il est premier
        print(num)