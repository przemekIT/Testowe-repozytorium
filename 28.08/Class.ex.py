#https://materials.itstep.org/content/42e06dbc-a07f-4662-a8d6-0699bc43b892/pl

# Zadanie 1
class Human():
    def __init__(self, imie = "", nazwisko = "", data = "", numer = "", miasto = "", kraj = "", adres = ""):
        self.imie = imie
        self.nazwisko = nazwisko
        self.data = data
        self.numer = numer
        self.miasto = miasto
        self.kraj = kraj
        self.adres = adres

    def input_data(self):
        self.nimie = input("Podaj imie: ")
        self.nazwisko = input("Podaj nazwisko: ")
        self.data = input("Podaj data: ")
        self.numer = input("Podaj numer: ")
        self.miasto = input("Podaj miasto: ")
        self.kraj = input("Podaj kraj: ")
        self.adres = input("Podaj adres: ")

    def display_data(self):
        print(f"Imie : {self.imie}")
        print(f"Nazwisko : {self.nazwisko}")
        print(f"Data : {self.data}")
        print(f"Numer : {self.numer}")
        print(f"Miasto : {self.miasto}")
        print(f"Kraj : {self.kraj}")
        print(f"Adres : {self.adres}")

    # Gettery, settery
    def get_imie(self):
        return self.imie
    
    def set_imie(self, imie):
        if imie != "Ilir" and imie != "Edis":
            self.imie = imie
        else:
            print("Imienia nie mozna ustawic")

h1 = Human()
print(h1.__dict__)
h1.input_data()
print(h1.__dict__)

# Zadanie 2

