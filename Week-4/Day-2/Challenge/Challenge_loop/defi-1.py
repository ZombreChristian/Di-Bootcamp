number = int(input("Entrer un nombre : "))
taille_liste = int(input("Entrer la taille de la liste : "))

liste = []

for i in range (1, taille_liste+1):
    liste.append(number*i) 
print("Liste =",liste)