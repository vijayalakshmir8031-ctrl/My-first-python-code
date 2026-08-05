def Addition(a, b):
    return a + b

def Subtraction(a, b):
    return a - b

def Multiplication(a, b):
    return a * b

def Division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

def menu():
    print("simple calculator")
    print("1.Addition:")
    print("2.Subtraction:")
    print("3.Multiplication:")
    print("4.Division:")
    print("5.Exit")

while True:
    menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Addition:",Addition(num1, num2))

    elif choice == 2:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Subtraction:",Subtraction(num1, num2))

    elif choice == 3:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Multiplication:",Multiplication(num1, num2))

    elif choice == 4:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Division:",Division(num1, num2))

    elif choice == 5:
        print("Exiting the program.")
        break

def menu():
    print("Banking System")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

balance = 0
