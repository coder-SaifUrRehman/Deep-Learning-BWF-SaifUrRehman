favorite_places = {
    "Saifi": ["Paris", "New York", "UK"],
    "Ahmed": ["Singapore", "Germany"],
    "Ali": ["Pakistan", "India"]
}

for name, places in favorite_places.items():
    print(name + "'s favorite places are:")
    for place in places:
        print("\t",place)
    print("Next Person")
