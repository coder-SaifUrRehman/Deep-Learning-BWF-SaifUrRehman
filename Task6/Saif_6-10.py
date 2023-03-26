
favorite_num = {
    "Ali": [5,4,3],
    "Ahmad": [5,4,3],
    "bilal": [5,4,3],
    "Baber": [5,4,3],
    "Saifi": [5,4,3]
}

for name, numbers in favorite_num.items():
    print(name + " fav num are:")
    for number in numbers:
        print( "   "+ number)
    print()

