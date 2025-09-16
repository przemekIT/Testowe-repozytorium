class Human:
    licznik = 0

    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
        Human.licznik += 1

    @classmethod
    def ile_obiektow(cls):
        return Human.licznik
    

h1 = Human("Jan", 30)
h2 = Human("Anna", 25)

print("Liczha obiektów klasy Human:", Human.ile_obiektow())



