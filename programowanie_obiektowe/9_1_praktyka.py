class Human():
    def __init__(self, name = "", birth_date = "", phone = "", city= "", country ="", address = ""):
        self.name = name
        self.birth_date = birth_date
        self.phone = phone
        self.city = city
        self.country = country
        self.address = address

    def input_data(self):
        self.name = input("Podaj imię i nazwisko: ")
        self.birth_date = input("Podaj date urodzenia: ")
        self.phone = input("Podaj numer telefonu: ")
        self.city = input("Podaj miasto: ")
        self.country = input("Podaj kraj: ")
        self.address = input("Podaj adres: ")

    def display_data(self):
        print(f"Imię i nazwisko: {self.name}")
        print(f"Data urodzenia: {self.birth_date}")
        print(f"Telefon: {self.phone}")
        print(f"Miasto: {self.city}")
        print(f"Kraj: {self.county}")
        print(f"Adres: {self.address}")

    # Gettery, settery
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        if name != "Przemek" and name != "Krzysiek":
            self.name = name
        else:
            print("Imienia nie mozna ustawic")

h1 = Human()
print(h1.__dict__)
h1.input_data()
print(h1.__dict__)