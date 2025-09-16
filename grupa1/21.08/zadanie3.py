def usun_puste_linie(plik_we, plik_wy):
    with open(plik_we, "r", encoding="utf-8") as f:
        linie = f.readlines()

    print(linie)

    linie_bez_pustych = [l.strip() for l in linie]

    print(linie_bez_pustych)

    with open(plik_wy, "w", encoding="utf-8") as f:
        f.writelines(linie_bez_pustych)


usun_puste_linie("output.txt", "bez_pustych.txt")

    
# Tekst wejściowy
tekst = "        Dowolny tekst\n Dowolny tekst 2\n Dowolny tekst 3\n    "

# Usunięcie spacji
tekst_bez_spacji = tekst.strip()

# Zapis do pliku
with open("plik_bez_spacji.txt", "w") as plik:
    plik.write(tekst_bez_spacji)
    