#while loop
i = 1
while i<= 5:
    print(i)
    i += 1
sheep_count = 1
while sheep_count<= 10:
    print(f"sheep {sheep_count}")
    sheep_count += 1
#using break to exit a while loop
sheep_count = 1
while sheep_count<= 10:
    print(f"sheep {sheep_count}")
    if sheep_count == 5:
        print("thats enough counting")
        break
    sheep_count += 1   
#using continue to skip an iteration
sheep_count = 1
while sheep_count<= 10:
    if sheep_count == 5:
        sheep_count += 1
        continue
    print(f"sheep {sheep_count}")   
    sheep_count += 1
    #using while loop for user input
    pin = ""
    correct_pin = "1234"
    while pin != correct_pin:
        pin = input("enter your pin")
        if pin != correct_pin:
            print("incorrect pin. try again")
            print("pin accepted. you can proceed")

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