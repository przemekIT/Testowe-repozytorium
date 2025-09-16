def liczby_pierwsze(start, koniec):
    def czy_pierwsza(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
        
    for liczba in range(start, koniec + 1):
        if czy_pierwsza(liczba):
            yield liczba #generator zwraca kolejne liczby pierwsze

    
for p in liczby_pierwsze(10, 50):
    print(p)