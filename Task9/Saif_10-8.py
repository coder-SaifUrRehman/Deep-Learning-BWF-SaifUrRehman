filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename, 'r') as file:
            print(f"\nContents of {filename}:")
            c = file.read()
            print(c)
    except FileNotFoundError:
        print(f"The file '{filename}' couldn't be found.")
