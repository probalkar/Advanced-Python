# filter() : filter() function is used to filter the given iterables with the help of another function passed as an argument to test all the elements to be True or False.

# syntax: filter(function, iterable)

friends = [
    ("Rachel", 25),
    ("Monica", 27),
    ("Phoebe", 26),
    ("Joey", 29),
    ("Chandler", 28),
    ("Ross", 30)
]

age = lambda data: data[1] >= 27
friends_age = list(filter(age, friends))
print(friends_age)