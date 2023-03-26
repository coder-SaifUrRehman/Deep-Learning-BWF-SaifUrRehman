rivers = {
    'Neil': 'Egypt',
    'sindh': 'pk',
    'Mississippi ': 'United States',
	'Ganges ' : 'India'
}

for river, country in rivers.items():
    print("The " + river + " runs through" + country)

print("Rivers Names:")
for river in rivers.keys():
    print(river)

print("Countries Names: ")
for country in rivers.values():
    print(country)
