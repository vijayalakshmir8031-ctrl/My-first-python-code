L = [1,23,45,76,34]
total = 0
for num in L:
    total = total + num
    print(total)

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")