file_name = 'responses.txt'

print("Why do you like programming? Press \'ctrl + c\' to exit")

while True:
    answer = input()
    with open(file_name, 'a') as file_object:
        file_object.write(answer + '\n')
        print("Response written to file.")
