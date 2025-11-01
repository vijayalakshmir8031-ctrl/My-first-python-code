# tuple
my_name = ("element1", "element2", "element3")
print(type(my_name))
#set
my_set = {"element", "element", "element"}
print(type(my_set))
#empty set
empty_set = {"element1", "element2", "element3"}
empty_set = set()
print(empty_set)
#set operation
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2 #union
print(set1 | set2)
#intersection
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1 & set2
print(set1 & set2)
#difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1 - set2
print(set1 - set2)
#symmetric difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}
sym_diff_set = set1 ^ set2
print(set1 ^ set2)
#set method
family_set= {"shreedhar", "sindhu", "vijayalakshmi", "tarun"}
family_set.add("trisha")
print(family_set)
#remove
family_set= {"shreedhar", "sindhu", "vijayalakshmi", "tarun"}
family_set.remove("tarun")
print(family_set)
#discard
family_set= {"shreedhar", "sindhu", "vijayalakshmi", "tarun"}
family_set.discard("tarun")
print(family_set)
family_set= {"shreedhar", "sindhu", "vijayalakshmi", "tarun"}
family_set.clear()
print(family_set)
#output
<class 'tuple'>
<class 'set'>
set()
{1, 2, 3, 4, 5}
{3}
{1, 2}
{1, 2, 4, 5}
{'vijayalakshmi', 'shreedhar', 'trisha', 'sindhu', 'tarun'}
{'vijayalakshmi', 'shreedhar', 'sindhu'}
{'vijayalakshmi', 'shreedhar', 'sindhu'}
set()
# --- Variables ---
name = "Vijayalakshmi"
age = 20
marks = 85.5

# --- String operations ---
greeting = "Hello, " + name + "!"
print(greeting)
print("Your name in uppercase:", name.upper())

# --- List ---
subjects = ["Math", "Python", "AI", "DS"]
subjects.append("Java")   # adding new subject
print("Subjects list:", subjects)

# --- Tuple ---
college_info = ("AIML", "2nd Year", 2025)
print("College Info:", college_info)

# --- Mathematical operations ---
x = 10
y = 3
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Power:", x ** y)

# --- Set ---
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1 | set2
intersection_set = set1 & set2
difference_set = set1 - set2

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
#output
Hello, Vijayalakshmi!
Your name in uppercase: VIJAYALAKSHMI
Subjects list: ['Math', 'Python', 'AI', 'DS', 'Java']
College Info: ('AIML', '2nd Year', 2025)
Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333333335
Power: 1000
Union: {1, 2, 3, 4, 5, 6}
Intersection: {3, 4}
Difference: {1, 2}
# --- Tuple Program: All Tuple Operations ---

# 1. Creating tuples
student_info = ("Vijayalakshmi", 20, "AIML", 2025)
print("Student Info Tuple:", student_info)

# 2. Accessing elements
print("Name:", student_info[0])
print("Branch:", student_info[2])

# 3. Negative indexing
print("Last Element (using negative index):", student_info[-1])

# 4. Tuple Slicing
print("First 3 elements:", student_info[:3])

# 5. Nested Tuple
college = ("SU College", ("AIML", "CSE", "ECE"))
print("Nested Tuple:", college)
print("Second Department in Nested Tuple:", college[1][1])

# 6. Tuple Concatenation
marks = (85, 90, 88)
full_details = student_info + marks
print("Combined Tuple:", full_details)

# 7. Tuple Repetition
repeat_tuple = ("Python",) * 3
print("Repeated Tuple:", repeat_tuple)

# 8. Length of tuple
print("Length of student_info:", len(student_info))

# 9. Checking if element exists
print("Is 'AIML' in student_info?", "AIML" in student_info)
print("Is 'CSE' in student_info?", "CSE" in student_info)

# 10. Iterating through tuple
print("Iterating through student_info:")
for item in student_info:
    print("-", item)

# 11. Tuple with numbers and built-in functions
numbers = (10, 20, 5, 40, 30)
print("Numbers Tuple:", numbers)
print("Max value:", max(numbers))
print("Min value:", min(numbers))
print("Sum of all numbers:", sum(numbers))

# 12. Tuple unpacking
(name, age, branch, year) = student_info
print("Unpacked Values:")
print("Name:", name)
print("Age:", age)
print("Branch:", branch)
print("Year:", year)

# 13. Nested Tuples inside List
students = [
    ("Ravi", 19, "AIML"),
    ("Priya", 20, "CSE"),
    ("Manu", 21, "ECE")
]
print("\nList of Student Tuples:")
for s in students:
    print("Name:", s[0], "| Age:", s[1], "| Dept:", s[2])

# 14. Tuple inside a function
def student_details(student_tuple):
    print("\n--- Student Details from Function ---")
    for i in range(len(student_tuple)):
        print(f"Detail {i+1}:", student_tuple[i])

student_details(student_info)

# 15. Returning tuple from function
def calculate_marks(m1, m2, m3):
    total = m1 + m2 + m3
    avg = total / 3
    return (total, avg)

result = calculate_marks(85, 90, 88)
print("\nMarks Total and Average:", result)
print("Total:", result[0])
print("Average:", result[1])