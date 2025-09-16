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

class B:
    def who(self):
        print("B")

class C(A):
    def who(self):
        print("C")

class D(C, B): # dziedziczenie wielokrotne
    pass
    

d = D()
d.who()
print(D.mro())

# D(nic), print(C), print(B), print(A)

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
        raise NotImplementedError("Ta metoda powinna byc nadpisana w klasie potomnej")