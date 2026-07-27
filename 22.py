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