l = [1,34,67,89]
total = 0
for num in l:
  total = total + num
  print(total)

l = [1,34,67,89]
dl = []
for num in l:
  dl.append(num*2)
  print(dl)

students = ["varun", "viji", "Trisha"] 
marks = [100,25,89]
student_marks = {}
for i, student_name in enumerate(students):
  student_marks[student_name] = marks[i]  
print(student_marks)

student_marks = {"varun":100, "viji":25, "Trisha":89}
for student, marks in student_marks.items():
  print(f"{student}----{marks}")

student_marks = {"varun":100, "viji":25, "Trisha":89}
for student, marks in student_marks.keys():
  print(f"{student}----{marks}")

student_marks = {"varun":100, "viji":25, "Trisha":89}
for student, marks in studentmamrka_values():
  print(f"{student}----{marks}")