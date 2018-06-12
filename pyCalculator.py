# this is a simple python calculator that does not use NumPy
def menu():
    print('MENU')
    print('1: Add +')
    print('2: Subtract -')
    print('3: Multiply x')
    print('4: Division /')
    print('5: Square x^2')
    print('6: Exponent x^y')
    print('7: Square Root x^0.5')
    print('Press any other number to exit')
    print()


def addnums(x, y):
    return x + y


def subtractnums(x, y):
    return x - y


def multiplynums(x, y):
    return x * y


def dividenums(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    else:
        return x/y


def squarenums(x):
    return x * x


def exponentnums(x, y):
    return x ** y


def squarerootnums(x):
    return x ** 0.5


# main program starts here
choice = 0

while choice >= 0:
    print('Welcome to my simple pyCalculator!')
    print()
    # catch ValueError if num1 or num2 is not a number
    while True:
        try:
            num1 = float(input('Please enter a number: '))
            num2 = float(input('Enter a second number: '))
            break
        except ValueError:
            print("Please enter numbers only. Try again.")

    menu()
    # catch ValueError if choice is not an integer
    while True:
        try:
            choice: int = int(input('What operation would you like to perform? '))
            break
        except ValueError:
            print('You must enter an integer. Please try again.')
            menu()

    if choice == 1:
        print(str(num1) + " + " + str(num2) + " = " + str(addnums(num1, num2)))
        print()
    elif choice == 2:
        print(str(num1) + " - " + str(num2) + " = " + str(subtractnums(num1, num2)))
        print()
    elif choice == 3:
        print(str(num1) + " * " + str(num2) + " = " + str(multiplynums(num1, num2)))
        print()
    elif choice == 4:
        print(str(num1) + " / " + str(num2) + " = " + str(dividenums(num1, num2)))
        print()
    elif choice == 5:
        print(str(num1) + " ^ 2 = " + str(squarenums(num1)))
        print()
    elif choice == 6:
        print(str(num1) + " ^ " + str(num2) + " = " + str(exponentnums(num1, num2)))
        print()
    elif choice == 7:
        print("The square root of " + str(num1) + " = " + str(squarerootnums(num1)))
        print()
    else:
        choice = -1

# exit program
print()
print('Thank you for using my pyCalculator!')
print()
