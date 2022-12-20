def nombreParfait():
    nb = input("Entrez un nombre :")
    nb = int(nb)
    div =[]
    for i in range(1,nb):
        if nb%i ==0 :
            div.append(i)   
    somme = sum(div)
    if nb == somme:
        print(nb,"est un nombre parfait")
    else:
        print(nb," n'est pas un nombre parfait")    


nombreParfait()

