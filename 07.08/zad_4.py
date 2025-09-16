dane = (("Ania", 95),("Tomek", 80), ("Kasia", 100))
 
zwyciezca = max(dane, key= lambda x: x[1])
przegrany = min(dane, key= lambda x: x[1])

print(zwyciezca)
print(przegrany)

wyniki_zawodnikow = (('Ania', 95), ('Tomek', 80), ('Kasia', 100))
 
lista_zawodnikow = list(wyniki_zawodnikow)
lista_zawodnikow.sort(key = lambda x: x[1], reverse=True)

for zawodnik, wynik in lista_zawodnikow[:3]:
    print(f"{zawodnik}: {wynik}")