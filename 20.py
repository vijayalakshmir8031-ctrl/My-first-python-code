#Functions
def greet():
    print("Hello! Welcome to the Python course.")
greet()

def greet_user(name):
    print(f"Hello!,{name} Welcome to the Python course.")
    greet_user("Tarun")

def tables(num):
  for i in range(1,11):
    print(f"num x i = {num*i}")
  tables(2)

def marriage(boy,girl):
  print(f" boy is {boy}")
  print(f" girl is {girl}")
  print(f" boy married {girl}")
  
marriage("chandhan", "sneha")

def marriage(boy,girl="girl"):
  print(f" boy is {boy}")
  print(f" girl is {girl}")
  print(f" boy married {girl}")
  
marriage("chandhan")

def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info(age=25, name="Kumar")

def total_sum(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result

print(total_sum(1, 2, 3, 4))

def student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(name="Anand", age=22, course="

double = lambda x: x * 2
print(double(5))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

def outer_function(name):
    def inner_function():
        print(f"Hello, {name}!")
    inner_function()

outer_function("Anand")

def add(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add(num1, num2)
print("Sum =", result)

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))
print(check_even_odd(number))

def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print("Largest number is:", largest(x, y, z))

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime Number")
else:
    print("Not a Prime Number")

def user_name(name):

    print(f"hello,{name} wellcome to a python program")
print(user_name("Tarun"))

def add(a,b):
    print(f"the sum is:{a+b}")
(add(5,2))
(add(9,2))
(add(6,2))

def user_name(name):

    print(f"hello, {name} wellcome to a python program")
user_name("student")
user_name("Trisha")

name = "Global Name"
def greet():
    name = "Local Name"
    print(name)

greet()  
print(name)

def student_info(name,age):
    print(f"name:{name}, age:{age}")
student_info("Tarun",16)

def student_info(**detalis):
    student_name = input("enter a student name:")
    student_age = int(input("enter the student age:"))
    student_course = input("enter the student course:")
    student_city = input("enter a student city:")
    student_father_name = input("enter the student's father's name:")
    student_mother_name = input("enter the student's mother's name:")
    student_phone_no = int(input("enter the student's phone number:"))
    student_father_phone_no = int(input("enter the student's father's phone number:"))
    student_mother_phone_no = int(input("enter the student's mother's phone number:"))
    for key, value in detalis.items():
        print(f"{key}: {value}")
student_info()

def total_sum(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result

print(total_sum(1, 2, 3, 4))

def multiply(*numbers):
    result = 1
    for num in numbers:
        result *= num
    print(result)

multiply(2, 3, 4)

def integer(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(integer(6, 3, 4))

def largest_num(*numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

print(largest_num(4, 8, 1234, 8, 9))

def smallest_num(*args):
    smallest = args[0]
    for num in args:
        if smallest > num:
            smallest = num
    return smallest
print(smallest_num(4,5,6,7,8))


double = lambda x: x * 2
print(double(5))

multiple = lambda x: x * 8
print(multiple(3))


def add(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add(num1, num2)
print("Sum =", result)

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))
print(check_even_odd(number))

def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print("Largest number is:", largest(x, y, z))

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime Number")
else:
    print("Not a Prime Number")

print("===== Student Result =====")

name = input("Enter Student Name: ")

m1 = int(input("Enter Python Marks: "))
m2 = int(input("Enter Maths Marks: "))
m3 = int(input("Enter English Marks: "))

total = m1 + m2 + m3
average = total / 3

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A+")
elif average >= 75:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")

print("===== Electricity Bill =====")

name = input("Enter Customer Name: ")
units = int(input("Enter Units Consumed: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = (100 * 2) + (units - 100) * 3
else:
    bill = (100 * 2) + (100 * 3) + (units - 200) * 5

print("\nCustomer Name:", name)
print("Units:", units)
print("Bill Amount:", bill)

print("===== Shopping Bill =====")

item1 = float(input("Enter Price of Item 1: "))
item2 = float(input("Enter Price of Item 2: "))
item3 = float(input("Enter Price of Item 3: "))

total = item1 + item2 + item3

if total >= 1000:
    discount = total * 0.10
else:
    discount = 0

final = total - discount

print("\nTotal Amount:", total)
print("Discount:", discount)
print("Final Amount:", final)