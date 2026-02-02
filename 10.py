#Tuples
my_tuples = ("element1","element2","elemnt3")
number_tuples = (1,2,3)
print(number_tuples)
print(my_tuples)
print(type(my_tuples))
#accessing tuples element
fruits = ("mango","apple","banana")
print(fruits[1])
fruits = ("mango","apple","banana")
print(fruits[-1])
#slicing tuples
fruits = ("mango","apple","banana")
print(fruits[1:2])
#tuples operations
tuple1 = (1,2,3)
tuple2 = (4,5,6)
print(tuple1 + tuple2)
#Repitating tuple
fruits = ("mango",)
print(fruits * 4)
#tuple methods
#count()
my_tuple = (1,2,3,1,2,3)
print(my_tuple.count(1))
#index()
fruits = ("mango","apple","banana")
print(fruits.index("mango"))
#sets in python
#union
s1 = {1,2,3}
s2 = {3,4,5}
print(s1 | s2)
print(type(s1))
#intersection
s1 = {1,2,3}
s2 = {3,4,5}
print(s1 & s2)
#diffrence
s1 = {1,2,3}
s2 = {3,4,5}
print(s1 - s2)
#symmetric diffrence
s1 = {1,2,3}
s2 = {3,4,5}
print(s1 ^ s2)
#set methods
#add()
fruits_set = {"mango","apple","banana"}
fruits_set.add("papaya")
print(fruits_set)
#remove
fruits_set = {"mango","apple","banana"}
fruits_set.remove("mango")
print(fruits_set)
#discard
fruits_set = {"mango","apple","banana"}
fruits_set.discard("mango")
print(fruits_set)
#pop()
fruits_set = {"mango","apple","banana"}
fruits_set.pop()
print(fruits_set)
fruits_set = {"mango","apple","banana"}
fruits_set.clear()
print(fruits_set)