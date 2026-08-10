try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter a valid number.")

try:
    age = int(input("Enter your age: "))

    if age < 0:
        print("Invalid age.")
    elif age > 100:
        print("You are already over 100 years old.")
    else:
        years = 100 - age
        print(f"You will be 100 years old in {years} years.")

except ValueError:
    print("Invalid input. Please enter a number.")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")



