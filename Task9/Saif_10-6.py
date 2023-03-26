while True:
    try:
        n1 = int(input("Ente 1st number: "))
        n2 = int(input("Enter 2nd number: "))
        result = n1 + n2
        print(f"result is: {result}")
        break
    except ValueError:
        print("Invalid input! Please enter number.")
