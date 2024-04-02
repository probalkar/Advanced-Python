# super() function : super() function is used to call the parent class methods from the child class. It returns a temporary object of the superclass which allows us to call the superclass methods.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def area(self):
        return self.length * self.width
    
class Cuboid(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height
    
square = Square(5)
cuboid = Cuboid(5, 3, 2)

print(square.area())
print(cuboid.volume())