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


dane = (("Ania", 95),("Tomek", 80), ("Kasia", 100))
def update_player(tup, name, score):
    lst = [list(item) for item in tup]
    for item in lst:
        if item[0] == name:
            item[1] = score
            break
    return tuple(lst)

def aktualizuj_wynik(ranking, imie, nowy_wynik):
    lista_ranking = list(ranking)
    for i, (zawodnik, wynik) in enumerate(lista_ranking):
        if zawodnik == imie:
            lista_ranking[i] = (zawodnik, nowy_wynik)
            break
    return tuple(lista_ranking)

 
print(update_player(dane, "Ania", 50))
 
