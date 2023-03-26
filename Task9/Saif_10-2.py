file_name = 'learning_python.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

for l in lines:
    modified_line = l.replace('python', 'C')
    print(modified_line.strip())
