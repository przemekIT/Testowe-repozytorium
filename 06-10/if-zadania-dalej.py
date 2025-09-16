# Zadanie 1 szczesliwa liczba
# liczba = int(input("Podaj sześciocyfrową liczbę: "))

# if 99999 > liczba or liczba > 999999:
#     print("Podana liczba nie jest sześciocyfrowa!")
# else:
#     c1 = liczba % 1000000 // 100000
#     c2 = liczba % 100000 // 10000
#     c3 = liczba % 10000 // 1000
#     c4 = liczba % 1000 // 100
#     c5 = liczba % 100 // 10
#     c6 = liczba % 10
#     if c1 + c2 + c3 == c4 + c5 + c6:
#         print("Podana liczba jest szczęśliwa!")
#     else:
#         print("Podana liczba nie jest szczęśliwa :(")

# # zadanie 2 
# liczba = int(input("Podaj sześciocyfrową liczbę: "))

# if 99999 < liczba > 999999:
#     "Podana liczba nie jest sześciocyfrowa!"
# else:
#     c1 = liczba % 1000000 // 100000
#     c2 = liczba % 100000 // 10000
#     c3 = liczba % 10000 // 1000
#     c4 = liczba % 1000 // 100
#     c5 = liczba % 100 // 10
#     c6 = liczba % 10
#     nowa_liczba = c6*100000 + c5*10000 + c3*1000 + c4*100 + c2*10 + c1
#     print(f"{liczba} staje się {c6}{c5}{c3}{c4}{c2}{c1}")
#     print(nowa_liczba)

# zadanie dalej 1 wejscie do klubu
# wiek = int(input("Podaj swój wiek: "))
# zaproszenie = input("Czy masz zaproszenie? ('tak'/'nie') ")

# if wiek < 18:
#     print("Spływaj stąd małolacie!")
# elif 18 <= wiek < 21 and zaproszenie == 'nie':
#     print("Nie wejdziesz bez zaproszenia, młody.")
# elif 18 <= wiek < 21 and zaproszenie == 'tak':
#     print("Wchodź, ale nie nabałagań.")
# else:
#     print("Wchodź.")

# zadanie dalej 2 trojkat
# a = int(input("Podaj długość pierwszego boku: "))
# b = int(input("Podaj drugą długość boku: "))
# c = int(input("Podaj trzecią długość boku: "))

# if (a+b > c) and (b+c > a) and (a+c > b):
#     print("Z podanych długości można zbudować trójkąt!")
#     if a == b and b == c:
#         print("To trójkąt równoboczny!")
#     elif a == b or b == c:
#         print("To trójkąt równoramienny!")
#     else:
#         print("To trójkąt różnoboczny.")
# else:
#     print("Nie można z tych boków utworzyć trójkąta :(")

# zadanie dalej 3 system logowania
# login = input("Podaj nazwę użytkownika: ")
# password = input("Podaj hasło: ")

# if login == "admin" and password == "root123":
#     admin_pass = input("Podaj klucz administratora: ")
#     if admin_pass == "XYZ42":
#         print("Zalogowano jako administrator.")
# elif login == "user" and password == "pass123":
#     print("Zalogowano jako użytkownik.")
# elif login == "guest" and password == "":
#     print("Zalogowano jako gość.")
# else:
#     print("Błąd logowania.")

# zadanie dalej 4 data
dzień = int(input("Podaj dzień: "))
miesiąc = int(input("Podaj miesiąc: "))
rok = int(input("Podaj rok: "))

przestepny = (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0)
print(przestepny)