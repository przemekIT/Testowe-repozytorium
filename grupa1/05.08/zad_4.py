liczby = (3, 12, 456, 7, 89, 123, 5, 1000, 999, 42, 6, 777, 10000000)

statystyki = {}

for liczba in liczby:
    cyfry = len(str(abs(liczba)))

    statystyki[cyfry] = statystyki.get(cyfry, 0) + 1


print(statystyki)
