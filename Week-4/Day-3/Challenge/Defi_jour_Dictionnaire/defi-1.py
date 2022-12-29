mot = input("Entrer un mot : ")
letters = {}

for key, letter in enumerate(mot):
  if letter not in letters:
    letters[letter] = []
  letters[letter].append(key)

print(letters)