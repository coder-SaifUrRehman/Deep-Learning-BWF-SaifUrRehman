file_name = 'learning_python.txt'

with open(file_name) as file:
    contents = file.read()
    print(contents)

with open(file_name) as file:
    for line in file:
        print(line.rstrip())

with open(file_name) as file:
    lines = file.readlines()

for l in lines:
    print(l.rstrip())

