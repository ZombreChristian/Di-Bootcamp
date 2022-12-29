import random
def nombre():
    aleatoire = random.randrange(1,101)
    nb = int(input("Entrer un nombre compris entre (1,100) :"))
    if aleatoire == nb:
        print("Bravo, Vous avez réussi")
    else:
        print("Désolé, Vous avez echoué")    
    print("*************************")
    print(f"Le nombre entré est :{nb} et le nombre aleatoire est :{aleatoire}".format(nb,aleatoire))
    
nombre()    
    