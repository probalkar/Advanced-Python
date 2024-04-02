# assigning functions to variables : it's like having an alias for a function
#                                    assigning a function's name to a variable without the parentheses stores the memory address of the function in the variable, the memory address of the function may change after each execution of the program
#                                    the function can then be called using either the original function name or the alias variable name followed by parentheses

# Example 1:
def hello():
    print("Hello, world!")

hi = hello
print(hello)
print(hi)
hello()
hi()

# Example 2:
display = print
print(print)
print(display)
print("Hello, world!")
display("Hello, world!")