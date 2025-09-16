# https://itsteppledu.sharepoint.com/sites/PythonWtCzw22052025/Shared%20Documents/General/Zawodnicy_polimorfizm.pdf

class Zawodnik:
    licznik = 0

    def __init__(self, imie, nazwisko, rok_urodzenia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.rok_urodzenia = rok_urodzenia
        Zawodnik.licznik += 1
        self.id = Zawodnik.licznik

    def opis(self):
        return f"{self.imie} {self.nazwisko}, ur. {self.rok_urodzenia}"

    @classmethod
    def ile_zawodnikow(cls):
        return cls.licznik

    @staticmethod
    def czy_pelnoletni(rok_urodzenia):
        return 2025 - rok_urodzenia >= 18


class Pilkarz(Zawodnik):
    def __init__(self, imie, nazwisko, rok_urodzenia, pozycja):
        super().__init__(imie, nazwisko, rok_urodzenia)
        self.pozycja = pozycja

    def opis(self):
        return super().opis() + f" – Piłkarz ({self.pozycja})"


class Biegacz(Zawodnik):
    def __init__(self, imie, nazwisko, rok_urodzenia, rekord):
        super().__init__(imie, nazwisko, rok_urodzenia)
        self.rekord = rekord

    def opis(self):
        return super().opis() + f" – Biegacz (rekord {self.rekord}s)"


class Plywak(Zawodnik):
    def __init__(self, imie, nazwisko, rok_urodzenia, styl):
        super().__init__(imie, nazwisko, rok_urodzenia)
        self.styl = styl

    def opis(self):
        return super().opis() + f" – Pływak ({self.styl})"


class KlubSportowy:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.zawodnicy = {}

    def dodaj_zawodnika(self, zawodnik):
        self.zawodnicy[zawodnik.id] = zawodnik

    def szukaj_po_nazwisku(self, nazwisko):
        return [z for z in self.zawodnicy.values() if z.nazwisko == nazwisko]

    def statystyki(self):
        return {
            "Piłkarzy": sum(isinstance(z, Pilkarz) for z in self.zawodnicy.values()),
            "Biegaczy": sum(isinstance(z, Biegacz) for z in self.zawodnicy.values()),
            "Pływaków": sum(isinstance(z, Plywak) for z in self.zawodnicy.values()),
        }

    
klub = KlubSportowy("Olimpia")

z1 = Pilkarz("Jan", "Kowalski", 2000, "napastnik")
z2 = Biegacz("Adam", "Nowak", 2010, 12.3)
z3 = Plywak("Piotr", "Kowalski", 1995, "kraulem")

klub.dodaj_zawodnika(z1)
klub.dodaj_zawodnika(z2)
klub.dodaj_zawodnika(z3)

print("=== Opisy zawodników ===")
for z in klub.zawodnicy.values():
    print(z.opis())

print("\n=== Szukaj po nazwisku Kowalski ===")
for z in klub.szukaj_po_nazwisku("Kowalski"):
    print(z.opis())

print("\n=== Statystyki ===")
print(klub.statystyki())

print("\nŁącznie zawodników:", Zawodnik.ile_zawodnikow())
