while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 + num2
        print(f"The result is: {result}")
        
    except ValueError:
        print("Invalid input! Please enter a number.")
    finally:
        choice = input("Do you want to perform another addition? (yes/no) ")
        if choice == 'no':
            break

