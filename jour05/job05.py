semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

def phare(nb_marche, hauteur_marche):
    for j in range(len(semaine)):
        for i in range(nb_marche):
            total_hauteur = (i+1) * hauteur_marche * 2
            total_marche = (j+1) * nb_marche * 2

        total_hauteur = total_hauteur * (j+1)

        print(semaine[j] + " le gardien a monté " + str(total_marche) + " marche d'une hauteur de " + str(total_hauteur) + "m")


phare(123, 0.13)







