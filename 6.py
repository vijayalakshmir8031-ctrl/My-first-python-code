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