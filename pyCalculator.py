# this is a simple python calculator that does not use the numpy
def menu():
    print('MENU')
    print('1: Add +')
    print('2: Subtract -')
    print('3: Multiply x')
    print('4: Division /')
    print('Press any other number to exit')
    print()


def addnums(x,y):
    return x + y


def subtractnums(x,y):
    return x - y


def multiplynums(x,y):
    return x * y


def dividenums(x,y):
    return x/y


# main program starts here
choice = 0

while choice >= 0:
    print('Welcome to my simple pyCalculator')
    num1 = int(input('enter first number'))
    num2 = int(input('enter second number'))
    menu()
    choice: int = int(input('What do you want to do?'))

    if choice == 1:
        print(addnums(num1, num2))
    elif choice == 2:
        print(subtractnums(num1, num2))
    elif choice == 3:
        print(multiplynums(num1, num2))
    elif choice == 4:
        print(dividenums(num1, num2))
    else:
        choice = -1

# exit program
print('Thank you for using the calculator')
