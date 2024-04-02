class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

# inheriting from Animal class
class Rabbit(Animal):
    def run(self):
        print("Rabbit is running")
    
class Fish(Animal):
    def swim(self):
        print("Fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("Hawk is flying")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()