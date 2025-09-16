from collections import Counter
# import re

# # Tekst wejściowy
# tekst = "Dowolny tekst\n Dowolny tekst 2\n Dowolny tekst 3\n Dowolny tekst 4\n Dowolny tekst 5\n"
# file_name = "tekst.txt"

# # Zapisanie tekstu do pliku
# with open(file_name, "w", encoding="utf-8") as file:
#     file.write(tekst)

# # **Odczytanie tekstu z pliku**
# with open(file_name, "r", encoding="utf-8") as file:
#     content = file.read()


# # Usunięcie znaków interpunkcyjnych i podział na słowa
# words = re.findall(r'\b\w+\b', content.lower())

# # Liczenie wystąpień słów
# word_counts = Counter(words)

# most_common_words = word_counts.most_common(5)  # Top 5 najczęstszych słów
# print("Najczęściej występujące słowa:")
# for word, count in most_common_words:
#     print(f"{word}: {count}")

def najczestsze_slowa(plik, n=5):
    with open(plik, "r", encoding = "utf-8") as f:
        slowa = f.read().lower().split()

    licznik = Counter(slowa)
    for slowo, ile in licznik.most_common(n):
        print(slowo, "->", ile)

najczestsze_slowa("output.txt", 5)