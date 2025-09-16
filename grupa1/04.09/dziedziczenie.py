# 1. Wstęp
# klasa bazowa
class Animal:
    def speak(self):
        print("Some sound...")

# klasa pochodna
class Dog(Animal):
    def speak(self): # nadpisanie metody
        print("Woof")

    def aport(self):
        print("Aporting...")

# klasa pochodna
class Cat(Animal):
    def milk(self):
        print("Drinking milk...")


a = Animal()
d = Dog()
c = Cat()

a.speak()
d.speak()
c.speak()

# 2. Konstruktor i super()
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id


p = Person("Przemek")
s = Student("Ala", 123)
print(s.name)
print(s.student_id)

# 3. Typy dziedziczenia

# 3.a Dziedziczenie pojedyncze, jedna klasa bazowa -> jedna klasa pochodna
class A:
    pass

class B(A):
    pass

# 3.b Dziedziczenie wielokrotne (tutaj działa MRO)
class A:
    def who(self):
        print("A")

class B(A):
    def who(self):
        super().who()
        print("B")

class C(A):
    def who(self):
        super().who()
        print("C")

class D(C, B):# dziedziczenie wielokrotne
    def who(self):
        super().who()
        print("D")
    
d = D()
d.who()
print(D.mro())

# D (nic), print(C), print(B), print(A)

class X:
    def __init__(self):
        print("X init")

class Y(X):
    def __init__(self):
        super().__init__()
        print("Y init")

class Z(X):
    def __init__(self):
        super().__init__()
        print("Z init")

class A(Y, Z):
    def __init__(self):
        super().__init__()
        print("A init")

a = A()

# (A), (Y), (Z), (X)

# 4. Polimorfizm
class Zwierze:
    def daj_glos(self):
        print("Zwierze")

class Pies(Zwierze):
    pass

class Kot(Zwierze):
    pass



# Przyklad 2Polimorficzne wywolania
zwierzeta = [Pies(), Kot(), Zwierze()]

for z in zwierzeta:
    print(z.daj_glos())


class Kaczka:
    def odglos(self):
        print("Kwa")

class Samochod:
    def odglos(self):
        print("Brum")

def zrob_odglos(obiekt):
    print(obiekt.odglos())


zrob_odglos(Kaczka())
zrob_odglos(Samochod())


# Przyklad 3
class Platnosc:
    def zaplac(self, kwota):
        raise NotImplementedError("Zaimplementuj tę metodę w klasie potomnej.")

class PlatnoscKarta(Platnosc):
    def zaplac(self, kwota):
        return f"Platnosc {kwota} PLN kartą zaakceptowana."

class PlatnoscPayPal(Platnosc):
    def zaplac(self, kwota):
        return f"Płatnosc {kwota} PLN przez PayPal zaakceptowana"

class PlatnoscBlik(Platnosc):
    def zaplac(self, kwota):
        return f"Płatnosc {kwota} PLN przez Blik zaakceptowana"


def wykonaj_platnosc(platnosc: Platnosc, kwota):
    print(platnosc.zaplac(kwota))

# Polimorficzne wywolania
wykonaj_platnosc(PlatnoscKarta(), 100)
wykonaj_platnosc(PlatnoscPayPal(), 250)
wykonaj_platnosc(PlatnoscBlik(), 50)




