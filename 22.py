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
