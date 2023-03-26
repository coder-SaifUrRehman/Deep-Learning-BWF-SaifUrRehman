file_name = 'guest_book.txt'

while True:
    name = input("What is your name? Press \'ctrl + c\' to quit.. ")
    print(name + " Welcome!")
    with open(file_name, 'a') as file_object:
        file_object.write(name + '\n')
