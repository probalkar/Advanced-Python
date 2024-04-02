# method chaining : Method chaining is a technique that allows multiple methods to be called on a single object in a single line of code.

class Calculator:
    def __init__(self, value):
        self.value = value

    def add(self, num):
        self.value += num
        return self

    def subtract(self, num):
        self.value -= num
        return self

    def multiply(self, num):
        self.value *= num
        return self

    def divide(self, num):
        self.value /= num
        return self

    def display(self):
        print(f"Current value: {self.value}")


# Create an instance of the Calculator class with an initial value of 10
calc = Calculator(10)

# Perform method chaining to add 5, subtract 3, multiply by 2, and divide by 4
calc.add(5).subtract(3).multiply(2).divide(4)

# Display the final value
calc.display()