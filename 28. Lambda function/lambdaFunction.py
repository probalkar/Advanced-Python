# lambda function : function written in one line with lambda keyword
#                   accepts any number of arguments
#                   think of it as a shortcut for defining simple functions
#                   lambda functions are used when you require a nameless function for a short period of time

# syntax: lambda arguments: expression

double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name + " " + last_name
age_check = lambda age: True if age >= 18 else False
print(double(5))
print(multiply(5, 6))
print(add(5, 6, 7))
print(full_name("Probal", "Kar"))
print(age_check(20))