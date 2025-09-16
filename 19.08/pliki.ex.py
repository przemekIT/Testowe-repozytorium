# https://itsteppledu.sharepoint.com/sites/PythonWtCzw22052025/Shared%20Documents/General/Pliki.pdf

# Zadanie 1
with open("tekst.txt", "r", encoding="utf-8") as f:
    text = f.read()

# liczba linii
line_count = len(text.splitlines())

# liczba słów
word_count = len(text.split())

# liczba znaków
char_count = len(text)

print("Liczba linii:", line_count)
print("Liczba słów:", word_count)
print("Liczba znaków:", char_count)

# Zadanie 2
# otwieramy plik źródłowy
with open("tekst.txt", "r", encoding="utf-8") as plik:
    with open("kopia.txt", "w", encoding="utf-8") as kopia:
        for linia in plik:
            kopia.write(linia)

print("Plik został skopiowany do 'kopia.txt'")
...
def kopiuj_plik(oryginal, kopia):
    with open(oryginal, "r", encoding="utf=8") as f:
        zawartosc = f.read()
    
    with open(kopia, "w", encoding = "utf=8") as f:
        f.write(zawartosc)

kopiuj_plik("tekst.txt", "kopia_druga.txt")