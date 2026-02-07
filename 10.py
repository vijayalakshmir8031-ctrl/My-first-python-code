#Tuples
my_tuples = ("element1","element2","elemnt3")
number_tuples = (1,2,3)
print(number_tuples)
print(my_tuples)
print(type(my_tuples))
#accessing tuples element
fruits = ("mango","apple","banana")
print(fruits[1])
fruits = ("mango","apple","banana")
print(fruits[-1])
#slicing tuples
fruits = ("mango","apple","banana")
print(fruits[1:2])
#tuples operations
tuple1 = (1,2,3)
tuple2 = (4,5,6)
print(tuple1 + tuple2)
#Repitating tuple
fruits = ("mango",)
print(fruits * 4)
#tuple methods
#count()
my_tuple = (1,2,3,1,2,3)
print(my_tuple.count(1))
#index()
fruits = ("mango","apple","banana")
print(fruits.index("mango"))
#sets in python
#union
s1 = {1,2,3}
s2 = {3,4,5}
print(s1 | s2)
print(type(s1))
#intersection
s1 = {1,2,3}
s2 = {3,4,5}
print(s1 & s2)
#diffrence
s1 = {1,2,3}
s2 = {3,4,5}
print(s1 - s2)
#symmetric diffrence
s1 = {1,2,3}
s2 = {3,4,5}
print(s1 ^ s2)
#set methods
#add()
fruits_set = {"mango","apple","banana"}
fruits_set.add("papaya")
print(fruits_set)
#remove
fruits_set = {"mango","apple","banana"}
fruits_set.remove("mango")
print(fruits_set)
#discard
fruits_set = {"mango","apple","banana"}
fruits_set.discard("mango")
print(fruits_set)
#pop()
fruits_set = {"mango","apple","banana"}
fruits_set.pop()
print(fruits_set)
fruits_set = {"mango","apple","banana"}
fruits_set.clear()
print(fruits_set)

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