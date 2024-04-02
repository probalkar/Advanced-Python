# map() : map() function returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)

# syntax: map(function, iterable)

phones = [
    ("Samsung", 600),
    ("Apple", 800),
    ("OnePlus", 500),
    ("Google", 700)
]

to_rupees = lambda data: (data[0], data[1] * 83.32)
phones_rupees = list(map(to_rupees, phones))
print(phones_rupees)