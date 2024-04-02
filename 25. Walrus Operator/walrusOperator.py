# walrus operator : The Walrus operator, also known as the assignment expression operator (:=), is a feature introduced in Python 3.8. It allows you to assign a value to a variable as part of an expression. This can be useful in situations where you want to assign a value and use it immediately within the same expression. The operator is represented by := and is typically used in conditional statements, loops, and function calls.

# Example 1:
# Without using walrus operator
# happy = True
# print(happy)

# # Using walrus operator
# print(happy := True)

# Example 2:
# Without using walrus operator
foods = list()
while True:
    food = input("Enter a food item (or 'quit' to exit): ")
    if food == "quit":
        break
    foods.append(food)
print(foods)

# Using walrus operator
foods = list()
while (food := input("Enter a food item (or 'quit' to exit): ")) != "quit":
    foods.append(food)
print(foods)