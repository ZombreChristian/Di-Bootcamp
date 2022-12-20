words = []
for i in range(1,8):
    user = input("Donnez 7 mots :")
    words.append(user)
        
user = input("Donnez un seul caractère :")
letter = user
for i in words:
    if letter in i:
        print("Index:",i.index(letter))
    else:
        break
    
    