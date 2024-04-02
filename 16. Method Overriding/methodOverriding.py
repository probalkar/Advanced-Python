# method overriding : Method overriding is a feature that allows a subclass to provide a specific implementation of a method that is already provided by its parent class.

class Animal:
    def sound(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def sound(self):
        print("The dog barks.")

class Cat(Animal):
    def sound(self):
        print("The cat meows.")

# Creating objects of the classes
animal = Animal()
dog = Dog()
cat = Cat()

# Calling the sound method of each object
animal.sound()  # Output: The animal makes a sound.
dog.sound()     # Output: The dog barks.
cat.sound()     # Output: The cat meows.