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
#code for python
numbers = (12, 45, 7, 89, 23)

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest element:", largest)

numbers = (10, 15, 20, 33, 44, 51)

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)
numbers = (5, 10, 15, 20, 25)

x = int(input("Enter a number: "))

if x in numbers:
    print("Element found")
else:
    print("Element not found")

numbers = (1, 2, 3, 4, 5)

reverse = numbers[::-1]

print("Original Tuple:", numbers)
print("Reversed Tuple:", reverse)
