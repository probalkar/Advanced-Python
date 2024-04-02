# sort() : sorts the list in place, works only with lists
# sorted() : returns a new sorted list, works with any iterable

# Example 1:
# students_list = ["Probal", "Awantika", "Smita"]
# print(students_list)
# students_list.sort()
# print(students_list)

# students_tuples = ("Probal", "Awantika", "Smita")
# print(students_tuples)
# print(sorted(students_tuples))

# Example 2:
# students = [
#     ("Probal", 20),
#     ("Awantika", 21),
#     ("Smita", 22)
# ]
# students.sort() # sorting alphabetically by name
# print(students)
# students.sort(reverse=True) # sorting alphabetically by name in reverse order
# print(students)
# students.sort(key=lambda ages: ages[1])  # sorting by age  
# print(students)
# students.sort(key=lambda ages: ages[1], reverse=True)  # sorting by age in reverse order
# print(students)

students = (
    ("Probal", 20),
    ("Awantika", 21),
    ("Smita", 22)
)

print(sorted(students)) # sorting alphabetically by name
print(sorted(students, reverse=True)) # sorting alphabetically by name in reverse order
print(sorted(students, key=lambda ages: ages[1])) # sorting by age
print(sorted(students, key=lambda ages: ages[1], reverse=True)) # sorting by age in reverse order