print("Welcome to the calculator of complex numbers!")

x, y = map(int, input("Enter real and imaginary parts of first complex number (separated by space): ").split())
a, b = map(int, input("Enter real and imaginary parts of second complex number (separated by space): ").split())

z1 = complex(x, y)
z2 = complex(a, b)

def case1():
    print("Addition of numbers:", z1 + z2)

def case2():
    print("Subtraction of numbers:", z1 - z2)

def case3():
    print("Multiplication of numbers:", z1 * z2)

def case4():
    print("Division of numbers:", z1 / z2 if z2 != 0 else "Error: Division by zero!")

options = {
    '1': case1,
    '2': case2,
    '3': case3,
    '4': case4,
}

while True:
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    case_number = input("Enter case number (1-4), or 5 to exit: ")

    if case_number == '5':
        print("Thank you for using the calculator!")
        break
    elif case_number in options:
        options[case_number]()
    else:
        print("Invalid input. Please enter a number between 1 and 5.")

