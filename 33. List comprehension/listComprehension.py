# list comprehension : a way to create a new list with less syntax
#                      can mimic certain lambda functions, easier to read
#                      list = [expression for item in iterable]
#                      list = [expression for item in iterable if condition]
#                      list = [expression if-else condition for item in iterable]

# Example 1:
squares = []
for i in range(1, 11):
    squares.append(i * i)
print(squares)

squares = [i * i for i in range(1, 11)]
print(squares)

# Example 2:
students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
passed_students = list(filter(lambda marks: marks >= 40, students))
print(passed_students)

passed_students = [marks for marks in students if marks >= 40]
print(passed_students)