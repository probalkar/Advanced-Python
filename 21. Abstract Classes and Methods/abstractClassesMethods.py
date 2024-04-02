# abstract classes : Abstract classes are classes that contain one or more abstract methods. Abstract classes may not be instantiated, and require subclasses to provide implementations for the abstract methods.
# abstract methods : Abstract methods are methods that are declared in an abstract class, but do not contain any implementation. The implementation is provided by the subclass that inherits from the abstract class.

from abc import ABC, abstractmethod

# abstract classes must have atleast one abstract method for it to be truly an abstract class and prevent them from being instantiated
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    def stop(self):
        print("This vehicle has stopped.")

class Car(Vehicle):
    def go(self):
        print("The car is moving.")

class Motorcycle(Vehicle):
    def go(self):
        print("The motorcycle is moving.")

# Creating instances of Car and Motorcycle
# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# Calling the go and stop methods of Car and Motorcycle
car.go()
car.stop()

motorcycle.go()
motorcycle.stop()

# vehicle.stop()