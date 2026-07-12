Example 1: Creating a dictionary of squares
numbers = [1, 2, 3, 4, 5]
squares_dict = {num: num ** 2 for num in numbers}
print(squares_dict)

Example 2: Converting a list of names to a dictionary of name lengths
names = ["Anand", "Geetha", "Kumar"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)

Example 3: Filtering cities with population above 10 lakhs (Localized Example)
city_population = {
    "Bengaluru": 84,
    "Mysuru": 11,
    "Hubballi": 9,
    "Mangaluru": 5
}
large_cities = {city: population for city, population in city_population.items() if population > 10}
print(large_cities)

Example 2: Splitting a string with commas
data = "apple,banana,mango"
fruits = data.split(",")
print(fruits)

Example 3: Limiting the number of splits
sentence = "Python is fun to learn"
words = sentence.split(" ", 2)
print(words)

numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print("Total sum:", total)

numbers = [1, 2, 3, 4, 5]
doubled = []

for num in numbers:
    doubled.append(num * 2)

print("Doubled List:", doubled)

foods = ["Dosa", "Idli", "Vada", "Bisibelebath"]

for food in foods:
    print(f"I like {food}")
