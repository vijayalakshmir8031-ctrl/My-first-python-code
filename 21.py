class Car:
    # Attributes
    def __init__(self, brand, model):
        self.brand = brand  # Instance variable
        self.model = model  # Instance variable

    # Method
    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

# Creating an object of the class
my_car = Car("Toyota", "Corolla")
my_car.display_info()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating objects
person1 = Person("Arjun", 30)
person2 = Person("Megha", 25)

person1.greet()
person2.greet()

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")

# Creating multiple objects
dog1 = Dog("Rex", "Golden Retriever")
dog2 = Dog("Bolt", "Beagle")

dog1.bark()
dog2.bark()

class Student:
    def __init__(self, name, usn, branch):
        self.name = name
        self.usn = usn
        self.branch = branch

    def display_details(self):
        print("----- Student Details -----")
        print("Name   :", self.name)
        print("USN    :", self.usn)
        print("Branch :", self.branch)

    def study(self):
        print(self.name, "is studying Python OOP.")

# Creating Object
student1 = Student("Rahul", "4SU23AI001", "AIML")

# Calling Methods
student

def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Current Balance:", self.balance)

# Creating Object
account = BankAccount("Anjali", 5000)
# Performing Operations
account.display_balance()
account.deposit(2000)
account.withdraw(3000)
account.display_balance()