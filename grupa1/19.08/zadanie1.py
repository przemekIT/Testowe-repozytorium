# def licz_statystyki(plik):
#     with open(plik, "r", encoding="utf-8") as f:
#         zawartosc = f.read()

#     linie = zawartosc.splitlines()
#     slowa = zawartosc.split()
#     znaki = len(zawartosc)

#     return len(linie), len(slowa), znaki

# linie, slowa, znaki = licz_statystyki("output.txt")
# print(f"Linie: {linie}, słowa: {slowa}, znaki: {znaki}.")

with open("tekst.txt", "r", encoding="utf-8") as plik:
    with open("kopia.txt", "w", encoding="utf-8") as kopia:
        for linia in plik:
            kopia.write(linia)
 
print("Plik został skopiowany do 'kopia.txt'")



def kopiuj_plik(oryginal, kopia):
    with open(oryginal, "r", encoding = "utf-8") as f:
        zawartosc = f.read()

    with open(kopia, "w", encoding = "utf-8") as f:
        f.write(zawartosc)


kopiuj_plik("tekst.txt", "kopia_druga_trzeciaśś.txt")