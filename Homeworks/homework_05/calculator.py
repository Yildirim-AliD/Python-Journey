# Develop an advanced calculator using custom functions instead of the built-in math module.

import my_math

def show_menu():
    print("\n--- Advanced Calculator (Custom Math Module) ---")
    print("1. Square Root")
    print("2. Power")
    print("3. Logarithm")
    print("4. Sine")
    print("5. Cosine")
    print("6. Tangent")
    print("7. Factorial")
    print("0. Exit")

while True:
    show_menu()
    choice = input("Choose an operation (0-7): ")

    if choice == '0':
        print("Exiting...")
        break

    elif choice == '1':
        num = float(input("Enter a number: "))
        print("Result:", my_math.square_root(num))

    elif choice == '2':
        base = float(input("Enter the base: "))
        exp = float(input("Enter the exponent: "))
        print("Result:", my_math.power(base, exp))

    elif choice == '3':
        num = float(input("Enter a number: "))
        base = input("Enter base (press Enter for natural log): ")
        if base == "":
            print("Result:", my_math.logarithm(num))
        else:
            print("Result:", my_math.logarithm(num, float(base)))

    elif choice == '4':
        angle = float(input("Enter angle in degrees: "))
        print("Result:", my_math.sine(angle))

    elif choice == '5':
        angle = float(input("Enter angle in degrees: "))
        print("Result:", my_math.cosine(angle))

    elif choice == '6':
        angle = float(input("Enter angle in degrees: "))
        print("Result:", my_math.tangent(angle))

    elif choice == '7':
        num = int(input("Enter a non-negative integer: "))
        print("Result:", my_math.factorial(num))

    else:
        print("Invalid choice. Please try again.")
