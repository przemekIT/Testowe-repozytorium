import library

class Zegar:
    def __init__(self, typ_zasilania=None, producent=None, rok_produkcji=None, cena=None, typ=None):
        self.typ_zasilania = typ_zasilania
        self.producent = producent
        self.rok_produkcji = rok_produkcji
        self.cena = cena
        self.typ = typ

    def wprowadz(self, *args):
        if len(args) == 5:
            self.typ_zasilania, self.producent, self.rok_produkcji, self.cena, self.typ = args
        elif len(args) == 1 and isinstance(args[0], dict):
            dane = args[0]
            self.typ_zasilania = dane.get("typ_zasilania")
            self.producent = dane.get("producent")
            self.rok_produkcji = dane.get("rok_produkcji")
            self.cena = dane.get("cena")
            self.typ = dane.get("typ")
        else:
            print("Błędne dane wejściowe!")

    def __str__(self):
        return (f"Typ zasilania: {self.typ_zasilania}, Producent: {self.producent}, Rok produkcji: {self.rok_produkcji}, Cena: {self.cena}, Typ: {self.typ}")
    

    def wiek(self, aktualny_rok = 2025):
        if self.rok_produkcji:
            return aktualny_rok - self.rok_produkcji
        return None

z = Zegar()
z.wprowadz("Bateria", "Casio", 2020, 150, "Cyfrowy")
print(z.wiek())
print(z)