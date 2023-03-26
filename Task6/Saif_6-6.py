fav_langs = {
    'Saifi': 'python',
    'Ali': 'c',
    'Ahmed': 'ruby',
    'Bilal': 'python',
}

poll = ['Saifi', 'Ali', 'Ahmed', 'Bilal', 'noor', 'Shafiq']

for person in poll:
    if person in fav_langs.keys():
        print("Thank you, " + person+ " for taking part in the poll!")
    else:
        print(person + " what's your favorite pro_lang?")
