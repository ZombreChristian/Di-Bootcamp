magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Tranformer la liste en chaine
a = " ".join(magician_names)
# Tranformer la chaine en liste
b = a.split()

def show_magicians(liste):
    print("List of magician:")
    for x in liste:
        print(x)
    return liste    
    


# Changer les nom des magician
def make_great():
    dct = {b[i]: b[i + 1] for i in range(0, len(b), 2)}
    listes = []
    for key, value in dct.items():
        # changer les nom par "The great"
        value= "The great"
        #Ajouter les changement dans une liste
        listes.append(key)
        listes.append(value)
        
        # Tranformer la liste en dictionnaire
        doc = {listes[i]: listes[i + 1] for i in range(0, len(listes), 2)}
    val =[] 
    #parcourir le dictionnaire
    for key, value in doc.items():
        #mettre chaque valeur dans une liste
        val.append(f"{key} {value}".format(key,value))
     #returner la liste   
    return val

""" def show_magicians():
    return make_great() """

print(show_magicians(magician_names))
show_magicians = make_great

print(show_magicians ()) 

