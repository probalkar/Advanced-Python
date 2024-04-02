# **kwargs : parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs):
    print("Hello", end=" ")
    for value in kwargs.values():
        print(value, end=" ")

hello(title = "Mr.", firstName = "Probal", lastName = "Kar")
print("\n")
hello(title = "Mrs.", firstName = "Awantika", middleName = "Vasant", lastName = "Ankushe")