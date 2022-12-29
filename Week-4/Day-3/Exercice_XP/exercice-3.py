brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue',
        'Spain': 'red',
        'US': ['pink', 'green']
    }
}

brand['number_stores'] = 2

print("Zaras clients are men, women, children and home")

brand['country_creation'] = 'Spain'

if "international_competitors" in brand:
    brand['international_competitors'].append("Desigual")
    
del brand['creation_date']

a = brand['international_competitors'][-1]
print("The last international competitor's is :",a)

b = (", ".join(brand['major_color']['US']))
print("The major clothes colors in the US:",b)

print("length of the dictionary:",len(brand))

c= (", ".join(brand.keys()))
print("The keys of the dictionary:",c)

more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}

brand.update(more_on_zara)

d = brand['number_stores']
print("The value of the key number_stores :",d)



