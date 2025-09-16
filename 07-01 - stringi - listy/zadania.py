# # Zadanie 1
# text = input("Wpisz tekst, a zostanie odwrócony: ")

# print(text[::-1])


# # Zadanie 2
# text = input("Wpisz tekst: ")

# lista_cyfr = [char for char in text if char.isdigit()]
# lista_liter = [char for char in text if char.isalpha()]

# print("W tekście występuje tyle cyfr:", len(lista_cyfr))
# print("W tekście występuje tyle liter:", len(lista_liter))


# # Zadanie 3
# text = input("Wpisz tekst: ")
# symbol = input("Podaj symbol do wyszukania w tekście: ")

# print("Symbol", symbol, "występuje w tekście tyle razy:", text.count(symbol))


# # Zadanie 4
# text = input("Wpisz tekst: ")
# word = input("Podaj słowo, które chcesz wyszukać: ")

# print(f"Słowo '{word}' pojawia się w tekście tyle razy: {text.count(word)}")


# # Zadanie 5
# text = input("Wpisz tekst: ")
# word = input("Wpisz szukane słowo: ")
# replacement = input("Wpisz słowo, którym chcesz zastąpić: ")

# print("Oto zamieniony tekst:")
# print(text.replace(word, replacement))


#  Zadanie 2.2


# # Zadanie 2.3

# lista_liczb = input("Podaj listę liczb oddzielonych spacją: ")

# liczby = lista_liczb.split()

# suma = 0

# for liczba in liczby:
#     liczba_int = int(liczba)
#     suma += liczba_int

# średnia = suma/len(liczby)

# print("Suma wszystkich liczb wynosi:", suma)
# print("Średnia wszystkich liczb wynosi:", round(średnia, 2))
