file_name = 'guest.txt'
name = input("What is your name? ")
with open(file_name, 'w') as file:
    file.write(name)
