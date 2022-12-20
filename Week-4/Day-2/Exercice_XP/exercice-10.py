# List of sandwich
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
# creation of empty list
finished_sandwiches = []
# create "p" which will allow us to determine the exact number of sandwiches prepared
n = 0
# remove ready-made sandwiches
while sandwich_orders !=[]:
    ajout =input("What sandwich did you finish making?")
    if ajout in sandwich_orders:
        sandwich_orders.remove(ajout)
        finished_sandwiches.append(ajout)
        n = n + 1

# Print the ready-made sandwiches
for i in range(0, n):
    print("I made your ",finished_sandwiches[i])