# https://materials.itstep.org/content/b352f985-f1d5-4404-9cf4-105d9e6db057/pl

# Zadanie 1

# Zadanie 2
class Kola:
    def opis_kol(self):
        return "Samochod ma 4 kola"

class Silnik:
    def opis_silnika(self):
        return "Silnik to V12"
    
class Drzwi:
    def opis_drzwi(self):
        return "Jest dwu drzwiowy"
    
class Kolor:
    def opis_koloru(self):
        return "Jest w kolorze czarnym"
    
class Samochod(Kola, Silnik, Drzwi, Kolor):
    def __init__(self, marka):
        self.marka = marka

    def opis(self):
        return (f"Samochód marki {self.marka}.\n"
                f"{self.opis_kol()}\n"
                f"{self.opis_silnika()}\n"
                f"{self.opis_drzwi()}\n"
                f"{self.opis_koloru()}")

auto = Samochod("Toyota")
print(auto.opis())

# Zadanie 3

class Pet:
    def __init__(self, name, cecha):
        self.name = name
        self.cecha = cecha

    def show(self):
        print(f"Imie: {self.name}")

    def type(self):
        print(f"Cecha: {self.cecha}")

class Dog(Pet):
    def __init__(self, name):
        super().__init__(name, "pies domowy")
    
    def sound(self):
        print("Hau Hau")

class Cat(Pet):
    def __init__(self, name):
        super().__init__(name, "Kot domowy")
    
    def sound(self):
        print("Miou Miou")

class Parrot(Pet):
    def __init__(self, name):
        super().__init__(name, "Papuga")
    
    def sound(self):
        print("Kooo!")

class Hamster(Pet):
    def __init__(self, name):
        super().__init__(name, "Chomik syryjski")

    def sound(self):
        print("Piks Piks")
    
dog = Dog("Reksio")
cat = Cat("Vincent")
parrot = Parrot("Squishi")
hamster = Hamster("Felek")

for x in [dog, cat, parrot, hamster]:
    x.show()
    x.type()
    x.sound()
    print("-------\n--------")


# Zadanie 4
class Employer:
    def Print(self):
        print("This is Employer class")


class President(Employer):
    def Print(self):
        print("This is President class")


class Manager(Employer):
    def Print(self):
        print("This is Manager class")


class Worker(Employer):
    def Print(self):
        print("This is Worker class")

employers = [Employer(), President(), Manager(), Worker()]

for emp in employers:
    emp.Print()

# Zadanie 5

class Employer:
    def __init__(self, age):
        self.age = age

    def Print(self):
        print("This is Employer class")

    def __str__(self):
        return f"Employer, wiek: {self.age}"

    def __int__(self):
        return self.age


class President(Employer):
    def Print(self):
        print("This is President class")

    def __str__(self):
        return f"President, wiek: {self.age}"


class Manager(Employer):
    def Print(self):
        print("This is Manager class")

    def __str__(self):
        return f"Manager, wiek: {self.age}"


class Worker(Employer):
    def Print(self):
        print("This is Worker class")

    def __str__(self):
        return f"Worker, wiek: {self.age}"


# --- Test ---
president = President(55)
manager = Manager(40)
worker = Worker(25)

# użycie __str__
print(president)   # President, wiek: 55
print(manager)     # Manager, wiek: 40
print(worker)      # Worker, wiek: 25

# użycie __int__
print(int(president))  # 55
print(int(manager))    # 40
print(int(worker))     # 25
