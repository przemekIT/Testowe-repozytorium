# https://materials.itstep.org/content/29a52953-5e91-4b44-a664-bd9b5a97fe4e/pl?inline=true

# Zadanie 1
class Car:
    def __init__(self, marka, model, rok, moc, kola, drzwi):
        self.marka = marka
        self.model = model
        self.rok = rok
        self.moc = moc
        self.kola = kola
        self.drzwi = drzwi

    def __str__(self):
        return f"{self.marka} {self.model}, {self.rok} rok, {self.moc} KM, {self.kola} kol, {self.drzwi} drzwi."
    
    def __lt__(self, other):
        return self.rok < other.rok
    
    def __eq__(self, other):
        return (self.marka, self.model, self.rok) == (other.marka, other.model, other.rok)
    

car1 = Car("Mercedes", "Klasa A", 2018, 120, 4, 5)
car2 = Car("Audi", "A8L", 2025, 450, 4, 5)

print(car1)
print(car2)

print(car1<car2)
print(car1 == car2)

# Zadanie 2
class Book:
    def __init__(self, tytul, autor, rok_wydania, cena):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.__cena = None
        self.cena = cena

    @property
    def cena(self):
        return self.__cena
    
    @cena.setter
    def cena(self, value):
        if value < 0:
            raise ValueError("Cena nie moze byc ujemna!")
        self.__cena = value
    
    def __str__(self):
        return f"'{self.tytul}' - {self.autor}, {self.rok_wydania}, cena: {self.cena} zl"
    
    def __lt__(self, other):
        return self.rok_wydania < other.rok_wydania
    
    def __eq__(self, other):
        return (self.tytul, self.autor) == (other.tytul, other.autor)
    
book1 = Book("Baba", "Mirek", 2005, 10)
book2 = Book("Lalka", "Ola", 1995, 5)
book3 = Book("Rolki", "Max", 2020, 20)

print(book1)
print(book2)
print(book3)

print(book1 == book2)
print(book1 < book3)

# Zadanie 3
class Stadium:
    def __init__(self, nazwa, miasto, pojemnosc, rok_budowy):
        self.nazwa = nazwa
        self.miasto = miasto
        self.pojemnosc = pojemnosc
        self.rok_budowy = rok_budowy
    
    def __str__(self):
        return f"Stadion: {self.nazwa}, {self.miasto}, pojemnosc:{self.pojemnosc}, rok: {self.rok_budowy}"
    
    def __len__(self):
        return len(self.nazwa)
    
    def __add__(self, other):
        if isinstance(other, Stadium):
            return self.pojemnosc + other.pojemnosc
        elif isinstance(other, int):
            return self.pojemnosc + other
        return NotImplemented
    
    def __call__(self):
        return f"{self.nazwa} w {self.miasto}, {self.pojemnosc} miejsc"
    
s1 = Stadium("Narodowy", "Warszawa", 50000, 2012)
s2 = Stadium("Brukselski", "Bruksela", 34000, 2008)
print(s1)
print(s2)
print(len(s1))
print(s1 + s2)
print(s1 + 5000)
print(s1())