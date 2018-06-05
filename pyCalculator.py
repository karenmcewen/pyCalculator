# this is a simple python calculator that does not use the numpy
choice = 0
print('MENU')
print('1: Add +')
print('2: Subtract -')
print('3: Multiply x')
print('4: Division /')
print('0: Exit')
print()
print()
choice: int = int(input('What do you want to do?'))
print(choice)
num1 = int(input('enter first number'))
num2 = int(input('enter second number'))
if choice == 0:
    print('ending')

elif choice == 1:
    print(num1 + num2)

elif choice == 2:
    print(num1 - num2)
elif choice == 3:
    print(num1 * num2)
elif choice == 4:
    print(num1 / num2)
else:
    print('that is not a valid option')
