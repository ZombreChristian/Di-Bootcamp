def saisie():
    utilisateur = input("Saisissez une chaine :")
    taille = len(utilisateur)
    if taille < 10:
        print("Chaine pas assez longue")
    else:
        print("Chaine trop longue")

    print("Le premier caractère :"+utilisateur[0]+"\n Le dernier caracère :"+utilisateur[taille-1]) 

    
saisie()            