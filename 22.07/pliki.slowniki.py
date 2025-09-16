# Zadanie 1
zakupy = [ 
    "Jan,Kawa,12.5", 
    "Anna,Herbata,9.0", 
    "Jan,Cukier,5.0", 
    "Anna,Kawa,12.5", 
    "Jan,Herbata,9.0", 
]

def analiza_zakopow(zakupy):
    wydatki = {}
    produkty = {}

    for t in zakupy:
        klient, produkt, cena = t.split(",")
        cena = float(cena)

        # Sumowanie wydatkow
        wydatki[klient] = wydatki.get(klient, 0) + cena

        # Zliczanie produktow
        produkty[produkt] = produkty.get(produkt, 0) + 1

    # Najwieksze koszta
    print(wydatki.values())
    max_wydatek = max(wydatki.values())
    top_klienci = [k for k, v in wydatki.items() if v == max_wydatek]

    # Posortowane produkty
    produkty_sorted = dict(sorted(produkty.items(), key = lambda x: x[1], reverse = True))

    print(produkty_sorted)
    print(max_wydatek)
    print(top_klienci)

    print(wydatki)
    print(produkty)

analiza_zakopow(zakupy)

# Zadanie 2
