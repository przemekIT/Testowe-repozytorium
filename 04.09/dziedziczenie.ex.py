# https://materials.itstep.org/content/94d6b240-c1ca-462b-a1cc-80f2c56311ab/pl

# Zadanie 1

class Human:
    def __init__(self, imie, lat):
        self.imie = imie
        self.lat = lat
    
    def introduce(self):
        return f"Nazwam sie {self.imie} i mam {self.lat} lat."

class Builder(Human):
    def __init__(self, imie, lat, specjalizacja):
        super().__init__(imie, lat)
        self.specjalizacja = specjalizacja
    
    def work(self):
        return f"{self.imie} buduje {self.specjalizacja}."

class Sailor(Human):
    def __init__(self, imie, lat, statek):
        super().__init__(imie, lat)
        self.statek = statek

    def sail(self):
        return f"{self.imie} pływa na statku o nazwie {self.statek}."

class Pilot(Human):
    def __init__(self, imie, lat, samolot):
        super().__init__(imie, lat)
        self.samolot = samolot

    def fly(self):
        return f"{self.imie} lata dla linii {self.samolot}."

b = Builder("Jan", 25, "domy")
s = Sailor("Aga", 28, "Mika")
p = Pilot("Mariusz", 30, "LOT")

print(b.introduce())
print(b.work())

print(s.introduce())
print(s.sail())

print(p.introduce())
print(p.fly())

# Zadanie 2

class Passport:
    def __init__(self, kraj, passport_number, name):
        self.kraj = kraj
        self.passport_number = passport_number
        self.name = name

    def intro(self):
        return f"{self.name} pochodzi z kraju {self.kraj}. "

class ForeignPassport(Passport):
    def __init__(self, kraj, passport_number, name, foreing_passport_number, visa):
        super().__init__(kraj, passport_number, name)
        self.visa = visa
        self.foreing_passport_number = foreing_passport_number
    
    def intro(self):
        return (f"{super().intro()}, Foreign Passport No: {self.foreing_passport_number},"
                f"Visa: {' , '.join(self.visa)}")
    
fp = ForeignPassport("Poland", "PL1234", "Jan Kowalsi", "FR2132", ["USA", "Canada"])
print(fp.intro())