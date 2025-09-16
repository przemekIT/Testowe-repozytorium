# ###### CZ 2 #####
# # Zadanie 1
# tekst = "alpha beta omega 123."

# # 1. Wielkie litery na początku zdań (bardzo prosto, nieidealnie)
# zdania = tekst.split('. ')
# tekst_poprawiony = '. '.join([zdanie.capitalize() for zdanie in zdania])

# # 2. Liczenie liczb (szukamy cyfr)
# liczba_liczb = 0
# for znak in tekst:
#     if znak.isdigit():
#         liczba_liczb += 1

# # 3. Liczenie znaków interpunkcyjnych
# interpunkcja = ",.!?:;…"
# liczba_interpunkcji = 0
# for znak in tekst:
#     if znak in interpunkcja:
#         liczba_interpunkcji += 1

# # 4. Liczenie wykrzykników
# liczba_wykrzyknikow = tekst.count('!')

# # Wyniki
# print("Poprawiony tekst:")
# print(tekst_poprawiony)
# print("\nLiczba liczb:", liczba_liczb)
# print("Liczba znaków interpunkcyjnych:", liczba_interpunkcji)
# print("Liczba wykrzykników:", liczba_wykrzyknikow)

# # Zadanie 2
# lista = input("Wpisz liczby całkowite, oddzielając je spacjami: ")
# lista = lista.split()                # zamiana na listę stringów
# lista = [int(x) for x in lista]      # zamiana każdego elementu na liczbę całkowitą

# # Wprowadzenie liczby do policzenia
# liczba = int(input("Podaj liczbę, którą chcesz policzyć: "))

# # Liczenie wystąpień
# ile_razy = lista.count(liczba)

# # Wynik
# print("Liczba", liczba, "występuje na liście", ile_razy, "razy.")

# # Zadanie 3
# # Pobieranie listy liczb całkowitych od użytkownika
# lista = input("Wpisz liczby całkowite, oddzielając je spacjami: ")
# lista = lista.split()
# lista = [int(x) for x in lista]

# # Obliczanie sumy i średniej
# suma = sum(lista)
# srednia = suma / len(lista)

# # Wyświetlanie wyników
# print("Suma liczb:", suma)
# print("Średnia:", srednia)
