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
