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