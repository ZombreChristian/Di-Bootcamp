
"""
la formule pour obtenir une lettre cryptée sera: c = (x + n) mod 26
c est la valeur de place de la lettre cryptée
x est la valeur de lieu de la lettre réelle,
n est le nombre qui nous indique combien de positions de lettres nous devons remplacer.

D’autre part, pour décrypter chaque lettre, nous utiliserons la formule ci-dessous:

c = (x – n) mod 26

Comme vous pouvez le voir dans le programme, nous avons ajouté et soustrait 65 (pour les majuscules) et 97 (pour les minuscules) dans cette formule mathématique parce que la valeur ascii de 'A' est 65 et de 'a' est 97. 
La méthode ord() est utilisée pour obtenir la valeur ascii des lettres.
dechiffrement
cipher = cipher + chr((ord(char) – shift – 65) % 26 + 65)
"""

def encrypt():
    text = input("Entrer la chaine à crypter:  ")
    nombre = int(input("Entrer le nombre de décalage : "))
    print("La chaine originale: ", text) 
    
    cipher = ''
    for char in text:
        if char == ' ':
            cipher = cipher + char
        elif  char.isupper():
            cipher = cipher + chr((ord(char) + nombre - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + nombre - 97) % 26 + 97)
    print("La chaine cryptée: ", cipher)
 

def decrypt():
    text = input("Entrer la chaine à décrypter: ")
    nombre = int(input("Entrer le nombre de décalage : "))
    print("La chaine originale: ", text) 
    cipher = ''
    for char in text:
        if char == ' ':
            cipher = cipher + char
        elif  char.isupper():
            cipher = cipher + chr((ord(char) - nombre - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) - nombre - 97) % 26 + 97)
    print("La chaine decryptée: ",cipher)

def choix():
    print("1.Encrypter une chaine")
    print("2.Decrypter une chaine")

    option = input("Que vous voulez-vous faire ? :")
    option = int(option)
    if option == 1:
        encrypt()
    elif option == 2:
        decrypt()
    else:
        print("Ce n'est pas une option valide") 
choix()           

    


