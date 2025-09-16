# https://materials.itstep.org/content/0c48316e-5eca-4af2-9425-a87258c94e65/pl

# Zadanie 1

class Number:
    def __init__(self, value):
        # upewniamy się, że wartość to liczba
        if not isinstance(value, (int, float)):
            raise TypeError("Wartość musi być liczbą całkowitą lub zmiennoprzecinkową.")
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def __mul__(self, other):
        return Number(self.value * other.value)

    def __truediv__(self, other):
        if other.value == 0:
            raise ZeroDivisionError("Dzielenie przez zero!")
        return Number(self.value / other.value)

    def __str__(self):
        return str(self.value)

a = Number(10)
b = Number(5)

print(a + b)   
print(a - b)   
print(a * b)   
print(a / b)   

# Zadanie 2

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __mul__(self, other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __truediv__(self, other):
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

a = Fraction(1, 2)   # 1/2
b = Fraction(3, 4)   # 3/4

print("a + b =", a + b)  # 10/8
print("a - b =", a - b)  # -2/8
print("a * b =", a * b)  # 3/8
print("a / b =", a / b)  # 4/6

# Zadanie 3
class Library:
    def __init__(self, name, address, books=0):
        self.name = name
        self.address = address
        self.books = books

    def __str__(self):
        return f"Biblioteka '{self.name}', adres: {self.address}, liczba książek: {self.books}"

    # --- operatory arytmetyczne ---
    def __add__(self, value):
        return Library(self.name, self.address, self.books + value)

    def __sub__(self, value):
        return Library(self.name, self.address, self.books - value)

    def __iadd__(self, value):
        self.books += value
        return self

    def __isub__(self, value):
        self.books -= value
        return self

    # --- operatory porównania ---
    def __lt__(self, other):
        return self.books < other.books

    def __le__(self, other):
        return self.books <= other.books

    def __gt__(self, other):
        return self.books > other.books

    def __ge__(self, other):
        return self.books >= other.books

    def __eq__(self, other):
        return self.books == other.books

    def __ne__(self, other):
        return self.books != other.books

lib1 = Library("Biblioteka Miejska", "Warszawa", 1000)
lib2 = Library("Biblioteka Uniwersytecka", "Kraków", 800)

print(lib1)  
print(lib2)

# --- operatory arytmetyczne ---
lib1 += 200
print("Po dodaniu książek:", lib1)

lib2 -= 100
print("Po odjęciu książek:", lib2)

lib3 = lib1 + 50
print("Nowa biblioteka (kopia):", lib3)

# --- porównania ---
print("lib1 > lib2:", lib1 > lib2)
print("lib1 == lib3:", lib1 == lib3)
print("lib2 <= lib1:", lib2 <= lib1)

# Zadanie 4
from datetime import date, timedelta

class Date:
    def __init__(self, day, month, year):
        self._date = date(year, month, day)

    def __str__(self):
        return self._date.strftime("%d-%m-%Y")

    # różnica między datami (w dniach)
    def __sub__(self, other):
        if isinstance(other, Date):
            return abs((self._date - other._date).days)
        raise TypeError("Różnicę można obliczyć tylko między dwiema datami!")

    # dodawanie dni do daty
    def __add__(self, days):
        if isinstance(days, int):
            new_date = self._date + timedelta(days=days)
            return Date(new_date.day, new_date.month, new_date.year)
        raise TypeError("Do daty można dodać tylko liczbę dni (int)!")

    # dodajemy też odwrotne dodawanie: int + Date
    def __radd__(self, days):
        return self.__add__(days)

d1 = Date(1, 1, 2020)
d2 = Date(15, 1, 2020)

print("Data 1:", d1)
print("Data 2:", d2)

# różnica w dniach
print("Różnica dni:", d2 - d1)   # 14

# dodawanie dni
d3 = d1 + 40
print("Po dodaniu 40 dni:", d3)

# też działa odwrotnie
d4 = 100 + d1
print("Po dodaniu 100 dni:", d4)
