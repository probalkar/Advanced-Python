class Car:
    color = None

class Motorcycle:
    color = None

def paint_vehicle(vehicle, color):
    vehicle.color = color

car1 = Car()
car2 = Car()
car3 = Car()
motorcycle1 = Motorcycle()

paint_vehicle(car1, "red")
paint_vehicle(car2, "blue")
paint_vehicle(car3, "green")
paint_vehicle(motorcycle1, "yellow")

print(car1.color)
print(car2.color)
print(car3.color)
print(motorcycle1.color)