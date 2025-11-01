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