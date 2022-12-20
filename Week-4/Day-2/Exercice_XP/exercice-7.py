fruitUser = input("Saisissez vos fruits préférés separé de espace vide :")
liste = fruitUser.split()
print("liste = ",liste)

saisie = input("Entrez un nom de fruit :")
if saisie in liste:
    print("Vous avez choisi l’un de vos fruits préférés! Profitez-en!")
else:
    print("Vous avez choisi un nouveau fruit. J’espère que vous apprécierez") 