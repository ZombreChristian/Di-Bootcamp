
sandwich_orders = ["Pastrami sandwich", "Tuna sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Sabih sandwich",]
finished_sandwiches = []
n = 0
for i in sandwich_orders:
    if i == "Pastrami sandwich":
        sandwich_orders.remove("Pastrami sandwich")

while sandwich_orders != [] :
    ajout = input("What sandwich did you finish making? ")
    if ajout in sandwich_orders:
        sandwich_orders.remove(ajout)
        finished_sandwiches.append(ajout)
        n = n + 1
for i in range(0, n):
    print("I made your",finished_sandwiches[i])