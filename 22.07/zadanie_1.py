zakupy = [
    "Jan, Kawa, 12.5",
    "Anna, Herbata, 9.0",
    "Jan, Cukier, 5.0",
    "Anna, Kawa, 12.5",
    "Jan, Herbata, 9.0",
    "Przemek, Herbata, 26.50", 
]

def analiza_zakupow(zakupy):
    wydatki = {}
    produkty = {}

    for t in zakupy:
        klient, produkt, cena = t.split(",")
        print(t.split(","))
        print(klient)
        print(produkt)
        print(cena)
        cena = float(cena)

        # Sumowanie wydatków
        wydatki[klient] = wydatki.get(klient, 0) + cena

        # Zliczanie produktów
        produkty[produkt] = produkty.get(produkt, 0) + 1

    # Najwieksze koszta
    max_wydatek = max(wydatki.values())
    top_klienci = [k for k, v in wydatki.items() if v == max_wydatek]

    # Posortowane produkty
    produkty_sorted = dict(sorted(produkty.items(), key = lambda x: x[1], reverse = True))

    return wydatki, top_klienci, produkty_sorted


analiza_zakupow(zakupy)