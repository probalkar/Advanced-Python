# class variable - shared by all class instances, can be accessed through class name directly, can be modified for each class instance separately
# instance variables - unique for each class instance

class Car:
    
    wheels = 4

    def __init__(self, brand, model, year, color):
        self.brand = brand 
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f"{self.brand} {self.model} is driving")
    
    def stop(self):
        print(f"{self.brand} {self.model} has stopped")