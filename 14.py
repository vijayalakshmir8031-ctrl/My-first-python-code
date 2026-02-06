Basic for loop
Looping through a range of numbers
for i in range(5):
    print(i)
2️⃣ Looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
3️⃣ Looping through a tuple
numbers = (1, 2, 3)
for n in numbers:
    print(n)
4️⃣ Looping through a dictionary
student = {"name":"Viji", "age":20}
for key in student:
    print(key, student[key])
5️⃣ Looping through a string
word = "Python"
for letter in word:
    print(letter)
6️⃣ Using break
Stop the loop when a condition is met
for i in range(10):
    if i == 5:
        break
    print(i)
7️⃣ Using continue
Skip the current iteration
for i in range(5):
    if i == 2:
        continue
    print(i)
8️⃣ Using else with for
Runs after loop completes normally
for i in range(3):
    print(i)
else:
    print("Loop finished")
9️⃣ Nested for loop
Loop inside a loop
for i in range(3):
    for j in range(2):
        print(i, j)
1️⃣0️⃣ Using enumerate()
Get index + value while looping
fruits = ["apple", "banana"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
1️⃣1️⃣ Using zip()
Loop through multiple lists together
names = ["Viji", "Ravi"]
ages = [20, 21]
for name, age in zip(names, ages):
    print(name, age)
1️⃣2️⃣ List comprehension (shortcut)
squares = [x**2 for x in range(5)]
print(squares)