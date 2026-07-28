class Student:
    def student_marks(self):
        print("student marks are 99")
    def student_name(self):
        print("student name tarun")
    def student_age(self):
        print("student age is 15")

Student = Student()

Student.student_marks()
Student.student_name()
Student.student_age()

class Car:
    def start_engine(self):
        print("Engine started")

    def accelerate(self):
        print("Car accelerating")

    def brake(self):
        print("Car stopping")

car = Car()
car.start_engine()  # Abstracts complex internal workings
car.accelerate()
car.brake()

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # Private attribute

    def get_username(self):
        return self.username

    def check_password(self, password):
        return password == self.__password

user = User("dev_karnataka", "pass1234")
print(user.get_username())  # Access allowed
print(user.check_password("wrong_pass"))  # Returns False
print(user.check_password("pass1234"))  # Returns True

class Car:
    def start_engine(self):
        print("Engine started")

    def accelerate(self):
        print("Car accelerating")

    def brake(self):
        print("Car stopping")

car = Car()
car.start_engine()  # Abstracts complex internal workings
car.accelerate()
car.brake()

class Database:
    def __init__(self):
        self.__storage = {}

    def save_data(self, key, value):
        self.__storage[key] = value
        print(f"Data saved for {key}")

    def get_data(self, key):
        return self.__storage.get(key, "No data found")

db = Database()
db.save_data("user_101", {"name": "Raj", "age": 30})
print(db.get_data("user_101"))

class Student:
    def __init__(self):
        self.__marks = 90

    def show_marks(self):
        print(self.__marks)

s = Student()
s.show_marks()


class ATM:
    def __init__(self):
        self.__balance = 5000

    def balance(self):
        print(self.__balance)

a = ATM()
a.balance()

class Car:
    def start(self):
        print("Car Started")

car = Car()
car.start()

class Phone:
    def call(self):
        print("Calling...")

phone = Phone()
phone.call()

class Bank:
    def __init__(self):
        self.__balance = 5000
    def deposit(self, amount):
        self.__balance += amount
    def show(self):
        print("Balance:", self.__balance)

b = Bank()
b.deposit(1000)
b.show()

class Animal:
    def __init__(self,dog,cat):
        self.dog = dog
        self.cat = cat


    def sound(self):
        print(f"{self.dog} woof woof")
        print(f"{self.cat} meow meow")

Animal = Animal("dog", "cat")
Animal.sound()

class Animal():
    pass


class Dog (Animal):
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("dog makes: woof woof")

class Cat(Animal):
    def sound(self):
        print("cat makes: meow meow")

Dog = Dog()
Cat = Cat()
Dog.sound()
Cat.sound()

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Brand:", self.brand)


class Car(Vehicle):
    def start(self):
        print("Car starts with a key")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with a button")


car = Car("Toyota")
bike = Bike("Honda")

car.display()
car.start()

print()

bike.display()
bike.start()
