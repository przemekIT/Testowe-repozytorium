class Human:

    liczba_ludzi = 0

    def __init__(self, imie, nazwisko, data_ur, nr_tel, miasto, kraj, adres):
        self.imie = imie
        self.nazwisko = nazwisko
        self.data_ur = data_ur
        self.nr_tel = nr_tel
        self.miasto = miasto
        self.kraj = kraj
        self.adres = adres
        Human.liczba_ludzi += 1

    @classmethod
    def ile_ludzi(cls):
        return cls.liczba_ludzi
    
    #settery i gettery


Ludź1 = Human("Alan", "Romański", "1999-08-19", 432123321, "Wiedeń", "Austria", "Parkring 18")

for nazwa, wartosc in Ludź1.__dict__.items():
    print(f"{nazwa}: {wartosc}")

print("Aktualna liczba ludzi:", Human.ile_ludzi())



class City:

    def __init__(self, nazwa="", region="", kraj="", mieszkancy="", kod_pocztowy="", nr_kierunkowy=""):
        self.nazwa = nazwa
        self.region = region
        self.kraj = kraj
        self.mieszkancy = mieszkancy
        self.kod_pocztowy = kod_pocztowy
        self.nr_kierunkowy = nr_kierunkowy

    def input_data(self):
        self.nazwa = input("nazwa: ")
        self.region = input("region: ")
        self.kraj = input("kraj: ")
        self.mieszkancy = input("mieszkancy: ")
        self.kod_pocztowy = input("kod_pocztowy: ")
        self.nr_kierunkowy = input("nr_kierunkowy: ")

    def display_data(self):
        print(self.nazwa, 'nazwa')
        print(self.region, 'region')
        print(self.kraj, 'kraj')
        print(self.mieszkancy, 'mieszkancy')
        print(self.kod_pocztowy, 'kod_pocztowy')
        print(self.nr_kierunkowy, 'nr_kierunkowy')

City1 = City()