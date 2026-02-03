#Dictionaryy... 
Python
student = {
    "name": "Viji",
    "age": 20,
    "branch": "AIML"
}
Keys → unique, immutable (int, str, tuple)
Values → any data type
Ordered (Python 3.7+)
Mutable (changeable)
2️⃣ Dictionary Types
🔹 Empty Dictionary

d = {}
🔹 Single Dictionary
Copy code
Python
d = {"a": 1}
🔹 Multiple Values

d = {"a": 1, "b": 2, "c": 3}
🔹 Nested Dictionary

student = {
    "name": "Viji",
    "marks": {"maths": 90, "ai": 95}
}
3️⃣ Accessing Dictionary Values
🔹 Using Key

print(student["name"])
🔹 Using get()

print(student.get("age"))
✔ get() avoids error if key not found
4️⃣ Adding Elements
🔹 Add New Key-Value

student["college"] = "SIT"
5️⃣ Updating Dictionary
🔹 Update Existing Value

student["age"] = 21
🔹 update() method

student.update({"age": 22, "city": "Bangalore"})
6️⃣ Deleting Elements
🔹 pop()

student.pop("age")
🔹 del

del student["city"]
🔹 clear()

student.clear() 

keys()

student.keys()
🔹 values()

student.values()
🔹 items()

student.items()
🔹 get()

student.get("name")
🔹 pop()

student.pop("age")
🔹 popitem()

student.popitem()
🔹 update()

student.update({"grade": "A"})
🔹 copy()

new_student = student.copy()
🔹 fromkeys()

keys = ("a", "b", "c")
d = dict.fromkeys(keys, 0)