def make_sandwich(*ingredients):
    print("Make a sandwich with following ingredients:")
    for ingr in ingredients:
        print("\t"+ ingr)
    print("Sandwich is ready!")

make_sandwich("bread")
make_sandwich("meat", "cheese", "cabbage")
make_sandwich("cheese", "chicken", "bread", "Onion", "tomato")

