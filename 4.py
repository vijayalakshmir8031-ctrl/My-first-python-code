#list
fruits = ["apple", "banana", "cherry",]
print(fruits[0]) #output orange
print(fruits[-1]) #apple
fruits [1] = "orange" # changing a specific element
print(fruits)
fruits.reverse() #reverse the element of the list in place
print(fruits)
fruits.index("apple") 
print(fruits)
fruits.append("orange") #adding element
print(fruits)
fruits.insert(1, "kiwi")  # inserting an element at the specific index
print(fruits) 
fruits.remove("orange") # removing an element
print(fruits)
fruits.pop() # removing the last item
print(fruits)
fruits.pop(0) # removing the first item
print(fruits)
fruits.clear() #removing the all element
print(fruits) 
#list functions and methods
number = [5, 2, 9, 1 ,1, 1] 
print(sorted(number))
print(sum(number)) 
print(number.count(1))
number = [5, 2, 9, 1 ,1, 1] 
number.sort()
print(number)
#nested list
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          ]
print(matrix[1:2])