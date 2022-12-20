utilisateur = input("Saisissez votre mois entre (1 à 12) :")
utilisateur = int(utilisateur)
if utilisateur < 0 and utilisateur >12:
    print("Veillez saisir un entier entre 1 à 12")
else:    
    if utilisateur >=3 and utilisateur <= 5:
        print(utilisateur,"Correspond au printemps")  

    elif utilisateur >=6 and utilisateur <= 8:
        print(utilisateur,"Correspond à l'été")  

    elif utilisateur >=9 and utilisateur <=11 :
        print(utilisateur,"Correspond à l'automme")  
    else:
        print(utilisateur,"Correspond à l'hiver")                 
