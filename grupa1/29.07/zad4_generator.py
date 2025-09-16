def pierwsze_n(n):
    licznik = 0
    liczba = 2
    while licznik < n:
        # sprawdzamy czy liczba jest pierwsza
        for i in range(2, int(liczba ** 0.5) + 1):
            if liczba % i == 0:
                break
        else: # wykonuje sie, jesli petla nie zostala przerwana (czyli liczba jest pierwsza)
            yield liczba
            licznik += 1
        liczba += 1

for p in pierwsze_n(5):
    print(p)

