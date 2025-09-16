from datetime import date, timedelta

class Date:
    def __init__(self, day, month, year):
        self._date = date(year, month, day)

    # reprezentacja czytelna
    def __str__(self):
        return self._date.strftime("%d-%m-%Y")
    
    # róznica dat: date1 - date2 -> liczba dni
    def __sub__(self, other):
        if isinstance(other, Date):
            return abs((self._date - other._date).days)
        raise TypeError("Odjąć mozna tylko inną instancje klasy Date")

    # dodawanie dni: date + liczba
    def __add__(self, days):
        if isinstance(days, int):
            new_date = self._date + timedelta(days=days)
            return Date(new_date.day, new_date.month, new_date.year)
        raise TypeError("Do daty mozna dodac tylko liczbę dni (int)")
    
    # dodawanie odwrotne: liczba + date
    def __radd__(self, days):
        return self.__add__(days)
    
    # zwiększanie daty w miejscu: date += liczba
    def __iadd__(self, days):
        if isinstance(days, int):
            self._date += timedelta(days=days)
            return self
        raise TypeError("Do daty mozna dodac tylko liczbe dni (int)")
        
d1 = Date(4, 9, 2025)
d2 = Date(1, 1, 2025)

print("d1:", d1)
print("d2:", d2)

# roznica
print("Roznica dni:", d1 - d2)

# dodawanie
print("d1 + 10 dni:", d1 + 10)
print("5 dni + d2:", 5 + d2)

# +=
d2 += 30
print("d2 po += 30", d2)