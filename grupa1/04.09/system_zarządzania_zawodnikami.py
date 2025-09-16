from datetime import datetime

class Zawodnik:
    _licznik_id = 0
    _licznik_zawodnikow = 0

    def __init__(self, imie, nazwisko, rok_urodzenia):
        self._imie = None
        self._nazwisko = None
        self._rok_urodzenia = None

        # walidacja przez settery
        self.imie = imie
        self.nazwisko = nazwisko
        self.rok_urodzenia = rok_urodzenia

        # generowanie unikalnego ID
        Zawodnik._licznik_id += 1
        self._id = Zawodnik._licznik_id

        Zawodnik._licznik_zawodnikow += 1

    @property
    def imie(self):
        return self._imie
    
    @imie.setter
    def imie(self, value):
        if not value or not value.strip():
            raise ValueError("Imie nie moze byc puste!")
        self._imie = value.strip()

    @property
    def nazwisko(self):
        return self._nazwisko
    
    @nazwisko.setter
    def nazwisko(self, value):
        if not value or not value.strip():
            raise ValueError("Nazwisko nie moze byc puste!")
        self._nazwisko= value.strip()

    @property
    def rok_urodzenia(self):
        return self._rok_urodzenia
    
    @rok_urodzenia.setter
    def rok_urodzenia(self, value):
        aktualny = datetime.now().year
        if value > aktualny or value < 1900:
            raise ValueError(f"Rok urodzenia musi byc pomiedzy 1900 a {aktualny}.")
        self._rok_urodzenia = value

    @property
    def id(self):
        return self._id

    # metoda instancyjna
    def opis(self):
        return f"{self.imie} {self.nazwisko}, ur. {self.rok_urodzenia}"

    # metoda klasowa
    @classmethod
    def ile_zawodnikow(cls):
        return cls._licznik_zawodnikow

    @staticmethod
    def czy_polnoletni(rok_urodzenia):
        aktualny = datetime.now().year
        return (aktualny - rok_urodzenia) >= 18


# klasy potomne
class Pilkarz(Zawodnik):
    def __init__(self, imie, nazwisko, rok_urodzenia, pozycja):
        super().__init__(imie, nazwisko, rok_urodzenia)
        self.pozycja = pozycja

    def opis(self):
        return f"[Pilkarz] {self.imie} {self.nazwisko}, ur. {self.rok_urodzenia}, pozycja: {self.pozycja}"

class Biegacz(Zawodnik):
    def __init__(self, imie, nazwisko, rok_urodzenia, rekord_czasowy):
        super().__init__(imie, nazwisko, rok_urodzenia)
        self.rekod_czasowy = rekord_czasowy

    def opis(self):
        return f"[Biegacz] {self.imie} {self.nazwisko}, ur. {self.rok_urodzenia}, rekord czasowy: {self.rekod_czasowy}"

class Plywak(Zawodnik):
    def __init__(self, imie, nazwisko, rok_urodzenia, styl):
        super().__init__(imie, nazwisko, rok_urodzenia)
        self.styl = styl

    def opis(self):
        return f"[Biegacz] {self.imie} {self.nazwisko}, ur. {self.rok_urodzenia}, styl: {self.styl}"

    
class KlubSportowy:
    def __init__(self):
        self._zawodnicy = {}

    def dodaj_zawodnika(self, zawodnik: Zawodnik):
        self._zawodnicy[zawodnik.id] = zawodnik

    def szukaj_po_nazwisku(self, nazwisko):
        return [z for z in self._zawodnicy.values() if z.nazwisko.lower() == nazwisko.lower()]

    def statystyki(self):
        pilkarze = sum(isinstance(z, Pilkarz) for z in self._zawodnicy.values())
        biegacze = sum(isinstance(z, Biegacz) for z in self._zawodnicy.values())
        plywacy = sum(isinstance(z, Plywak) for z in self._zawodnicy.values())

        return {
            "piłkarze": pilkarze,
            "biegacze": biegacze,
            "plywacy": plywacy,
            "razem": len(self._zawodnicy)
        }

    def wszyscy_zawodnicy(self):
        return list(self._zawodnicy.values())


# TESTOWANIE
klub = KlubSportowy()

klub.dodaj_zawodnika(Pilkarz("Robert", "Lewandowski", 1988, "napastnik"))
klub.dodaj_zawodnika(Biegacz("Usain", "Bolt", 1938, "9.40"))
klub.dodaj_zawodnika(Plywak("Michael", "Phelps", 1985, "motylkowy"))
klub.dodaj_zawodnika(Pilkarz("Kylian", "Mbappe", 1998, "napastnik"))
klub.dodaj_zawodnika(Pilkarz("Kylian", "Bolt", 2010, "napastnik"))

# wszystkie opisy
print("=== Wszyscy zawodnicy ===")
for z in klub.wszyscy_zawodnicy():
    print(z.opis())

# wyszukiwanie
print("\n=== Szukamy zawodników o nazwisku 'Bolt' ===")
for z in klub.szukaj_po_nazwisku('BOLT'):
    print(z.opis())


# statystyki
print("\n === Statystyki klubu ====")
print(klub.statystyki())

# pelnoletni
print("\n === Status pelnoletnosci ====")
for z in klub.wszyscy_zawodnicy():
    status = "pelnoletni" if Zawodnik.czy_polnoletni(z.rok_urodzenia) else "niepelnoletni"
    print(f"{z.imie} {z.nazwisko} => {status}")

print("\nŁącznie zawodnikow utworzono:", Zawodnik.ile_zawodnikow())


    
    

