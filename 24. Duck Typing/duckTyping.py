# duck typing : concept where class of an object is less important than it's methods/attributes
#               class type is not checked, instead the presence of a given method or attribute is checked
#               if it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.

class Duck:
    def walk(self):
        print("The duck is walking.")

    def talk(self):
        print("The duck is quacking.")

class Chicken:
    def walk(self):
        print("The chicken is walking.")

    def talk(self):
        print("The chicken is clucking.")

class Person:
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the duck!")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
person.catch(chicken)