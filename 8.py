print("enter jug problem")
x = int(input("enter x: "))
y = int(input("enter y: "))
while true:
    rno = int(input("enter the rule no: "))
if rno == 1:
    if x < 4:
     x = 4
if rno == 2:
    if y < 3:
     y = 3
if rno == 5:
    if x > 0:
     x = 0
if rno == 6:
    if y > 0:
     y = 0
if rno == 7:
    if x + y < = 4 & y > o:
     x,y = 4,y-(4-x)
if rno == 8:
    if  x + y > = 3 & x > o:
     x,y = x-(3-y),3
if rno == 9:
    if x + y < = 4 & y > o:
     x,y = x + y,0
if rno == 10:
    if  x + y < = 3 & x > o:
     x,y = 0,x + y
print(f"current state: x={x},y={y}")

bill = float(input("Enter the bill amount: "))

if bill >= 5000:
    discount = bill * 0.20
elif bill >= 3000:
    discount = bill * 0.10
else:
    discount = 0

final_bill = bill - discount

print("Discount:", discount)
print("Final Bill:", final_bill)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Largest Number:", num1)
else:
    print("Largest Number:", num2)

num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

ch = input("Enter a character: ")

if ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")