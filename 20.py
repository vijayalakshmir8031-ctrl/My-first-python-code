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