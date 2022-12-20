names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user = input("Tapez votre nom :")
if user in names:
    print("Index :",names.index(user))
else:
    print("Desolé votre nom ne figure pas")