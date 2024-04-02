class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def __add__(self, other):   # overloading + operator for Fraction class
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)
    
    def __sub__(self, other):   # overloading - operator for Fraction class
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)
    
    def __mul__(self, other):   # overloading * operator for Fraction class
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)
    
    def __truediv__(self, other):   # overloading / operator for Fraction class
        num = self.num * other.den
        den = self.den * other.num
        return Fraction(num, den)
    
fr1 = Fraction(2, 3)
fr2 = Fraction(1, 2)

print(fr1)
print(fr2)
print(fr1 + fr2)
print(fr1 - fr2)
print(fr1 * fr2)
print(fr1 / fr2)