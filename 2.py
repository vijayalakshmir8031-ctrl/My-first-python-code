boy_name = input("boy name>>")
boy_age = int(input(" boy age "))
girl_name = input("girl name>>")
girl_age = int(input(" girl age "))
age_diff = (boy_age - girl_age)
print(f"{boy_name} loves {girl_name}. age diffrence is {age_diff}")
Basic for loop
Looping through a range of numbers
Copy code
Python
for i in range(5):
    print(i)
2️⃣ Looping through a list
Copy code
Python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
3️⃣ Looping through a tuple
Copy code
Python
numbers = (1, 2, 3)
for n in numbers:
    print(n)
4️⃣ Looping through a dictionary
Copy code
Python
student = {"name":"Viji", "age":20}
for key in student:
    print(key, student[key])
5️⃣ Looping through a string
Copy code
Python
word = "Python"
for letter in word:
    print(letter)
6️⃣ Using break
Stop the loop when a condition is met
Copy code
Python
for i in range(10):
    if i == 5:
        break
    print(i)
7️⃣ Using continue
Skip the current iteration
Copy code
Python
for i in range(5):
    if i == 2:
        continue
    print(i)
8️⃣ Using else with for
Runs after loop completes normally
Copy code
Python
for i in range(3):
    print(i)
else:
    print("Loop finished")
9️⃣ Nested for loop
Loop inside a loop
Copy code
Python
for i in range(3):
    for j in range(2):
        print(i, j)
1️⃣0️⃣ Using enumerate()
Get index + value while looping
Copy code
Python
fruits = ["apple", "banana"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
1️⃣1️⃣ Using zip()
Loop through multiple lists together
Copy code
Python
names = ["Viji", "Ravi"]
ages = [20, 21]
for name, age in zip(names, ages):
    print(name, age)
1️⃣2️⃣ List comprehension (shortcut)
Copy code
Python
squares = [x**2 for x in range(5)]
print(squares)