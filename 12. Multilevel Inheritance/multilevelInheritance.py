# multi-level inheritance : In multi-level inheritance, a class inherits from a class, which in turn inherits from another class.

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

# Child class inheriting from Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")

# Grandchild class inheriting from Dog
class Labrador(Dog):
    def fetch(self):
        print(f"{self.name} is fetching.")

# Creating an instance of Labrador
labrador = Labrador("Buddy")

# Calling methods from different levels of inheritance
labrador.eat()    # Output: Buddy is eating.
labrador.bark()   # Output: Buddy is barking.
labrador.fetch()  # Output: Buddy is fetching.