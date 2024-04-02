# *args : parameter that will all arguments in a tuple
#         useful so that a function can accept a varying amount of arguments

def add(*args):
    sum = 0
    for i in args:
        sum += i
    
    return sum

print(add(1,2,3))
print(add(1,2,3,4,5,6))