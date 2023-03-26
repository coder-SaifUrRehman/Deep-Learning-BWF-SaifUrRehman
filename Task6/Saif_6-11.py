cities = {
    'Isl': {'country': 'pk', 'population': 'XYZ', 'fact': 'XYZ'},
    'london': {'country': 'England', 'population': 'XYZ', 'fact': 'London is XYZZZ'},
    'BWP': {'country': 'PK', 'population': 'ABC', 'fact': 'Bwp is city of NAWAB\'s'}
}

for city, infor in cities.items():
    print("City: " + city.title())
    print("\tCountry: " + infor['country'])
    print("\tPopulation: " + infor['population'])
    print("\tFact: " + infor['fact'])

