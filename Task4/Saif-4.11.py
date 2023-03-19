pizzas = ['Cheesy Pizza', 'Chicken Fajita', 'Chicken BBQ']
friend_pizzas = pizzas[:]
pizzas.append('Tikka pizza')
friend_pizzas.append('italian pizza')

print("My pizzas are:")
for pizza in pizzas:
    print("\t",pizza)

print("My friend's pizzas are:")
for pizza in friend_pizzas:
    print("\t",pizza)
