var = [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
liste_numero = [int(i) for i in var]
print("Liste des numéros",liste_numero) 
var.sort(reverse=True)
print("Liste des nombres triés par ordre décroissant:",var)
somme_nombre = sum(var)
print("Somme des nombres =",somme_nombre)
liste_premier_dernier_nombre = [var[0],var[-1]]
print("Liste de premier et dernier numero",liste_premier_dernier_nombre)
liste_superieur_50 =[]

liste_superieur_50 = [int(i) for i in var if i >50 ]
print("liste_superieur_50",liste_superieur_50)

liste_inferieur_10 = [int(i) for i in var if i <10 ]
print("liste_inferieur_10",liste_inferieur_10)

liste_nombre_carre  = []
for i in range(0,len(var)):
    liste_nombre_carre.append(var[i]*var[i])
    
print("liste_nombre_carre ",liste_nombre_carre )

sans_doublons =[]
for i in var:
    if i not in sans_doublons:
        sans_doublons.append(i)
print("sans_doublons",sans_doublons)  

print("Plus grand nombre :",max(var))  
print("Plus petit nombre :",min(var))
max = var[0]

for i in var: 
    if i > max:
        max = i
print("max :",max)   
min = var[0]
for j in var: 
    if j < min:
        min = j
print("min :",min)   


s= 0
for i in var:
    s = s +i
print("somme =",s)
print("Moyenne =",s/len(var))   

a= []
b= []

for i in range(0,11):
    user1 = int(input("Entrer un numero compris entre (-100 et 100) :"))
    user2 = int(input("Entrer un nombre compris entre (-100 et 100) :"))
    a.append(user1)
    b.append(user2)
print("a =",a)
print("b =",b)

import random
nbr = []
nb = random.randrange(-100,101)
for i in range(0,11):
    nbr.append(nb)
print("nbr =",nbr)  
  
