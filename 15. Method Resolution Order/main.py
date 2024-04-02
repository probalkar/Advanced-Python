class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class Product:
    def __init__(self):
        print("Inside product constructor")

    def review(self):
        print("Reviewing the product")

#                  ⬇️
class SmartPhone(Phone, Product):   # constructor of Phone is called because it is inherited first
    pass

s = SmartPhone(20000, "Apple", "12MP")
s.buy()