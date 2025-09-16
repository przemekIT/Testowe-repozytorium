# Enkapsulacja
class Book:
    def __init__(self, cena):
        self.cena = cena # atrybut prywatny

    @property
    def cena(self):
        return f"Tu jest moj getter: {self.__cena}"
    
    @cena.setter
    def cena(self, value):
        if value < 30:
            print("Nie chce miec ponizej 30")
        else:
            self.__cena = value

ksiaska = Book(40)
print(ksiaska.cena)
ksiaska.cena = 25
print(ksiaska.cena)