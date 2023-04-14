import json
import random
import hashlib
import sys
req = "votre mot de passe doit contenir : une majuscule, un chiffre, un caractere special et un minumum de 8 caractere.\n!@#$%^&*"
# caractere :
lettre = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lettre_minuscule = lettre.lower()
nombre = "1234567890"
special = "!@#$%^&*"
caractere = lettre + lettre_minuscule + nombre + special
print(req)
m_d_p = ""
stock_password_file = "password_hash.txt"

def password(m_d_p): # vérifier la validiter d'un mot de passe
    while True:
        m_d_p = str(input("entrez votre mot de pass : "))
        nb_lettre = 0
        nb_nombre = 0
        nb_special = 0
        m_d_p_lenght = 0
        if len(m_d_p) >= 8:
            m_d_p_lenght = len(m_d_p)
        for i in m_d_p:
            if i in lettre:
                nb_lettre += 1
            elif i in nombre:
                nb_nombre += 1
            elif i in special:
                nb_special += 1

        if m_d_p_lenght >= 8 and nb_lettre > 0 and nb_nombre > 0 and nb_special > 0:
            m_d_p_hash = hashlib.sha256(m_d_p.encode("utf-8"))
            hashed_m_d_p = m_d_p_hash.hexdigest()
            with open(stock_password_file, "r") as f:
                read_file = f.readline()
                if hashed_m_d_p in read_file:
                    print("mdp deja enregistré")
                    break
            with open(stock_password_file, "a") as f:
                f.write(hashed_m_d_p +"\n")
                print("mdp ajouté avec succès")
            break
        else:
            print("mdp non valide")

def view_passwords():
    try:
        with open(stock_password_file, "r") as f:
            passwords = f.readlines()
            if len(passwords) == 0:
                print("Il n'y a aucun mot de passe enregistré.")
            else:
                print("Liste de tous les mots de passe enregistrés : ")
                for password in passwords:
                    print(password.strip())
    except FileNotFoundError:
        print("Il n'y a aucun mot de passe enregistré.")


while True:
    choice = input("pour entrez un nouveaux mot de passe tapez : 1 : \n pour consulter les mots de passe tapez : 2 : \n tapez 3 pour quitter le programe ")
    if choice == "1":
        password(m_d_p)
    if choice == "2":
        view_passwords()
    if choice == "3":
        sys.exit()




