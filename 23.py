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
while True:
    menu()
    choice = int(input("enter your choice"))
    if choice == 1:
        print("balance:", balance)
    elif choice == 2:
       amount = int(input("enter a amount to deposite"))
       balance += amount
    elif choice == 3:
        amount = int(input("enter a amount to withdraw"))
        balance -= amount
    elif choice == 4:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
        
def menu():
    print("\nSimple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter your choice (1-5): ")

    if choice in ['1', '2', '3', '4']:
        # Get two numbers from the user
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

    if choice == '1':
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
    elif choice == '5':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

def menu():
    print("Welcome to the Menu-Driven Program!")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Exit")

while True:
    menu()
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        print("You selected Option 1.")
    elif choice == '2':
        print("You selected Option 2.")
    elif choice == '3':
        print("You selected Option 3.")
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
class Student:
    def display(self):
        print("Student name: Vijay")
        print("Age: 20")

student1 = Student()
student1.display()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

employee1 = Employee("Rahul", 30000)
employee1.display()

class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

car1 = Car()
car1.start()
car1.drive()

class Bank:
    def __init__(self):
        self.__balance = 5000

    def show_balance(self):
        print("Balance:", self.__balance)

bank1 = Bank()
bank1.show_balance()

class Dog:
    def sound(self):
        print("Dog says: Bark")

class Cat:
    def sound(self):
        print("Cat says: Meow")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

from datetime import date, timedelta


class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.available = True


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = {}


class Library:
    def __init__(self):
        self.books = {}
        self.users = {}

    def add_book(self, book):
        self.books[book.book_id] = book

    def add_user(self, user):
        self.users[user.user_id] = user

    def borrow_book(self, user_id, book_id):
        user = self.users[user_id]
        book = self.books[book_id]

        if book.available:
            book.available = False
            due_date = date.today() + timedelta(days=7)
            user.borrowed_books[book_id] = due_date

            print(f"{user.name} borrowed '{book.title}'")
            print(f"Due Date: {due_date}")
        else:
            print("Book is not available.")

    def return_book(self, user_id, book_id):
        user = self.users[user_id]
        book = self.books[book_id]

        due_date = user.borrowed_books[book_id]
        return_date = date.today()

        late_days = max(0, (return_date - due_date).days)
        penalty = late_days * 10

        book.available = True
        del user.borrowed_books[book_id]

        print(f"{user.name} returned '{book.title}'")
        print(f"Late Days: {late_days}")
        print(f"Penalty: ₹{penalty}")

    def show_available_books(self):
        print("\nAvailable Books:")
        for book in self.books.values():
            if book.available:
                print(f"{book.book_id} - {book.title}")


# Creating library
library = Library()

# Adding books
library.add_book(Book("B101", "Python Programming"))
library.add_book(Book("B102", "Data Structures"))
library.add_book(Book("B103", "Machine Learning"))

# Adding users
library.add_user(User("U101", "Rahul"))
library.add_user(User("U102", "Priya"))

# Display available books
library.show_available_books()

# Borrow a book
library.borrow_book("U101", "B101")

# Display available books
library.show_available_books()

# Return the book
library.return_book("U101", "B101")

# Display final available books
library.show_available_books()
