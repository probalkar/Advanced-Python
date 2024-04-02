# multiple inheritance : In multiple inheritance, a class inherits from more than one class.

# Parent class 1
class Parent1:
    def method1(self):
        print("This is method 1 from Parent1")

# Parent class 2
class Parent2:
    def method2(self):
        print("This is method 2 from Parent2")

# Child class inheriting from Parent1 and Parent2
class Child(Parent1, Parent2):
    def method3(self):
        print("This is method 3 from Child")

# Creating an instance of Child class
obj = Child()

# Calling methods from Parent1, Parent2, and Child
obj.method1()
obj.method2()
obj.method3()