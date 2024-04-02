# reduce() : apply a function to an iterable and reduce it to a single cumulative value
#            performs function on first two elements, then on the result and the next element, and so on until only one element is left

# syntax: reduce(function, iterable)

from functools import reduce

letters = ["H", "E", "L", "L", "O"]
word = reduce(lambda x, y: x + y, letters)
print(word) # HELLO

factorial = [5, 4, 3, 2, 1]
result = reduce(lambda x, y: x * y, factorial)
print(result) # 120