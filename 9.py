#List...... 
#pop() remove the elemnt from the specific index
names = ["aiswarya","bhoomika","shubha"]
names.pop()
print(names)
names = ["aiswarya","bhooika","shubha"]
names.pop(0)
print(names)
#clear() remove all element from the list
names = ["aiswarya","bhooika","shubha"]
names.clear()
print(names)
#list function and method
#common function
names = ["aiswarya","bhooika","shubha"]
print(len(names))
#sortest list
names = ["aiswarya","bhooika","shubha"]
print(sorted(names))#list
names = ["aiswarya","bhooika","shubha"]
print(names)
#we can use here integers,strings,and other list
number = [1,"true",7.8]
print(number)
#accending list element
names = ["aiswarya","bhooika","shubha"]
print(names[0])
print(names[2])
#use can use negative index also
names = ["aiswarya","bhooika","shubha"]
print(names[-1])
print(names[-0])
#modifying list
#chenging a specific element
names[1] = "viju" 
print(names)
#adding elemnt
names = ["aiswarya","bhoomika","shubha"]
names.append("viju")
print(names)
#inserting a element
names = ["aiswarya","bhoomika","shubha"]
names.insert(2,"anusha")
print(names)
#removing elemnt
names = ["aiswarya","bhoomika","shubha"]
names.remove("aiswarya")
print(names)