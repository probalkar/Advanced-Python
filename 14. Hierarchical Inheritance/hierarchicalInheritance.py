# hierarchical inheritance : multiple derived classes from a single base class

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

# Usage
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Daisy")

print(dog.name + " says " + dog.speak())
print(cat.name + " says " + cat.speak())
print(cow.name + " says " + cow.speak())