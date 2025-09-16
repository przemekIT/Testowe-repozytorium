import string
from collections import Counter


# Pobranie tekstu od uzytkownika
tekst = input("Wprowadź tekst do analizy: ")

# Usuwanie interpunckji i zamiana na małe litery
tekst = tekst.lower()
for znak in string.punctuation:
    tekst = tekst.replace(znak, "")

# Rozdzielenie na slowa
slowa = tekst.split()

# Zliczenie wystąpien, stworzenie instancji klasy Counter
licznik = Counter(slowa)

# Wyswietlenie top 5 najczęstszych słów
print("Top 5 najczęstszych słów:")
for slowo, liczba in licznik.most_common(5):
    print(f"{slowo}: {liczba} razy")

# Rozbudowa - wyswietlenie pelnego slownika (uporządkowanego)
print("Wszystkie slowa (posortowane od najczęstszych): ")
for slowo, liczba in licznik.most_common():
    print(f"{slowo}: {liczba}")


