class Number:

    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
        print(f"Ustawiono wartość liczby")

    def __add__(self, other):
        return self.value + other.value
    
    def __sub__(self, other):
        return self.value - other.value

number1 = Number(10)
number2 = Number(20)
print(number1.value)
print(number1 + number2)
print(number1 - number2)

class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __add__(self, other):
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)
    
    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass
    
    def __str__(self):
        return f"{self.num}/{self.den}"
    
f1 = Fraction(1, 2)
f2 = Fraction(1, 3)

print(f1 + f2)


# class Date:

#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year