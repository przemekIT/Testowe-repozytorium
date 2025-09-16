# Enkapsulacja służy kontrolowaniu ustalania atrybutów (niechcianych)

class Book:
    def __init__(self, cena):
        self.cena = cena

    @property
    def cena(self):
        return f"To getter: {self.__cena}"
    
    @cena.setter
    def cena(self, value):
        if value < 30:
            print("Nie biorę takich tanich zabawek.")
        else:
            self.__cena = value


ksiazka = Book(50)
print(ksiazka.cena)
ksiazka.cena = 20
print(ksiazka.cena)