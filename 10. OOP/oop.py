from car import Car

car1 = Car("Lamborghini", "Aventador", 2021, "Red")
car2 = Car("Ford", "Mustang", 2023, "Silver")
car3 = Car("Ford", "Raptor", 2023, "Yellow")

# car1
print(car1.brand)
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.wheels)
car1.drive()
car1.stop()

# car2
print(car2.brand)
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.wheels)
car2.drive()
car2.stop()

# car3
car3.wheels = 6
print(car3.brand)
print(car3.model)
print(car3.year)
print(car3.color)
print(car3.wheels)
car3.drive()
car3.stop()

# accessing class variable through class name
print(Car.wheels)

# after changing class variable number of wheels of all cars change except those which were explicitly set
Car.wheels = 3
# car1
print(car1.wheels)

# car2
print(car2.wheels)

# car3
print(car3.wheels)