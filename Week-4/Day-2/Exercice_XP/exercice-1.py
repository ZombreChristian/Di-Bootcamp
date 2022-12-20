my_fav_numbers= [51245614,55024578,78512422,65221545]
my_fav_numbers.append("73254131")
my_fav_numbers.append("71551478")

taille = len(my_fav_numbers)
my_fav_numbers.remove(my_fav_numbers[taille-1])

friend_fav_numbers = [55263148,77454685,63225157]

my_fav_numbersfriend_fav_numbersour_fav_numbers = my_fav_numbers +friend_fav_numbers

print(my_fav_numbersfriend_fav_numbersour_fav_numbers )


