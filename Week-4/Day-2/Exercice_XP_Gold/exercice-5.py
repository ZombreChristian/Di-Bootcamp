chaine = "abcdefghijklmnopqrstuvwxyz"
voyelle ="aeiouy"
for i in range(0,len(chaine)):
    if chaine[i] in voyelle:
        print(chaine[i],"est une voyelle")
    else:
       print(chaine[i],"est une consonne")   