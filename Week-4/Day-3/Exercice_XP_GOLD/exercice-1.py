birthdays = {
    "Ali":'2003/06/12',
    "Franck":'2000/12/05',
    "Kader":'2001/05/18',
    "Fanta":'1999/02/21',
    "Severine":'2003/08/25'
}

print("Soyez les bienvenus ,Vous pouvez rechercher les anniversaires des personnes de la liste ! ")
user = input("Donnez le nom d'une personne dans le dictionnaire:")

reponse = birthdays[user]
print(f"{user} est né en {reponse}".format(user,reponse))