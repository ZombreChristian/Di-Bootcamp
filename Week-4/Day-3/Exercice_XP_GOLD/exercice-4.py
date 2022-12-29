""" items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
for x,y in items.items():
    print(x,y)
     """
items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
} 

for x in items.values():
    for j,k in x.items():
        print(j,k)
       