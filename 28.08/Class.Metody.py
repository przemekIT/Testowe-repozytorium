# Metody przeciazone

# 1. Konstruktor, __init__
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

h = Human("Jan", 30)

# 2. Reprezentacja czytelna, __str__
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Człowiek: {self.name}"
    
h = Human("Jan", 30)

print(h)

# 3. Reprezentacja techniczna, __repr__
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Human(name={self.name})"

h = Human("Jan", 30)

print(h)

# 4. Operator ==, __eq__
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    
h1 = Human("Krzysiek", 30)
h2 = Human("Krzysiek", 30)

print(h1 == h2)    

# 5.Operatory porowniania
class Human:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __lt__(self, other):
        return self.age < other.age
    
    def __gt__(self, other):
        return self.age > other.age
    
    def __le__(self, other):
        return self.age <= other.age
    
    def __ge__(self, other):
        return self.age >= other.age
    
    def __len__(self):
        return len(self.name)
    
h1 = Human("Krzysiek", 50, 200)
print(len(h1))

# 6. Dzialania arytmetyczne
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

# 7. Dostęp jak do listy, __getitem__, __setitem__

class Website:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        return self.data[key]

site = Website({"name": "OpenAI", "url": "wwww.openai.com"})
print(site["name"])

# 9. __call__

class Zegar:
    def __init__(self, producent):
        self.producent = producent

    def __call__(self):
        return f"Zegar produkcji: {self.producent}"

z = Zegar("Casio")
print(z())

# 10. __del__
class Human:
    def __del__(self):
        print("Obiekt usunięty")

h = Human()

# del h