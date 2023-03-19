my_food = ['Rice', 'vegetables', 'oreo']
friend_food = my_food[:]

print("My favorite foods are:")
for food in my_food:
    print("\t" + food)

print("\nMy friend's favorite foods are:")
for food in friend_food:
    print(f"\t" + food)
