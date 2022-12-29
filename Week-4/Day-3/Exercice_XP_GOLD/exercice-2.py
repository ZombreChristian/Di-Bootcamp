birthdays = {
    "Ali":'2003/06/12',
    "Franck":'2000/12/05',
    "Kader":'2001/05/18',
    "Fanta":'1999/02/21',
    "Severine":'2003/08/25'
}

liste = []

for key in birthdays.keys():
    liste.append(key)
for x in liste:
    print(x)
    
user = input("Donnez le nom d'une personne dans le dictionnaire:")

#for x in liste:
if user not in liste:
    print("Désolé, nous n’avons pas les informations d’anniversaire pour",user)
else:    
    reponse = birthdays[user]
    print(f"{user} est né en {reponse}".format(user,reponse)) 
