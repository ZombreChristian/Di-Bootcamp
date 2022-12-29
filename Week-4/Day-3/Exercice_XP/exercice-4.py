users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A = {}
for key, valeur_user in enumerate(users):
    disney_users_A[valeur_user] = key
print(disney_users_A)

disney_users_B = {}
for key, valeur_user in enumerate(users):
    disney_users_B[key] = valeur_user
print(disney_users_B)

disney_users_C = {}
a = sorted(users)
for key, valeur_user in enumerate(a):
    disney_users_C[valeur_user] = key
print(disney_users_C)

disney_users_D = {}
for key, valeur_user in enumerate(users):
    if "i" in valeur_user:
        disney_users_D[valeur_user] = key
print(disney_users_D)



disney_users_E = {}
for key, valeur_user in enumerate(users):
    if valeur_user.startswith(("M","P")):
        disney_users_E[valeur_user] = key
print(disney_users_E)
