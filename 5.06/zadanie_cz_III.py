# #zadanie1
# liczba = int(input(("Podaj sześciocyfrową liczbę: ")))

# if 100000 <= liczba <= 999999:
#     #rozbijamy na cyfry
#     c1 = liczba //100000 % 10
#     c2 = liczba //10000 % 10
#     c3 = liczba //1000 % 10
#     c4 = liczba //100 % 10
#     c5 = liczba //10 % 10
#     c6 = liczba % 10

#     first_sum = c1+c2+c3
#     second_sum = c4+c5+c6
#     if first_sum == second_sum:
#         print("To szczęśliwa liczba")
#     else:
#         print("To nie jest szczęśliwa liczba")
# else:
#     print("Błąd")

# #zadanie2
# liczba = int(input(("Podaj sześciocyfrową liczbę: ")))

# if 100000 <= liczba <= 999999:
#     #rozbijamy na cyfry
#     c1 = liczba //100000 % 10
#     c2 = liczba //10000 % 10
#     c3 = liczba //1000 % 10
#     c4 = liczba //100 % 10
#     c5 = liczba //10 % 10
#     c6 = liczba % 10

#     new_number = c6 * 100000 + c5 + 10000 + c3 * 1000 + c4*100 + c2 * 10 + c1
# else:
#     print("Błąd")

# #zadanie3
# numer_miesiąca =(input("podaj numer miesiąca: "))
# if numer_miesiąca == '1' or '2' or '12':
#     print("zima")
# elif '3'<=numer_miesiąca<='5': 
#     print("wiosna")
# elif '6'<= numer_miesiąca<='8':
#     print("lato")
# elif '9'<= numer_miesiąca<='11':
#     print("jesień")
# else:
#     print("zły numer miesiąca")

# #zadanie1:symulator wejścia do klubu
# wiek = int(input("podaj wiek: "))
# odpowiedz = input("Masz zaproszenie? ")
# if 18<= wiek and odpowiedz == 'tak':
#     print("wpuszczony")
# elif 21<=wiek:
#     print("wpuszczony bez zaproszenia")
# else:
#     print("nie wpuszczony")

# #zadanie2:sprawdzenie trójkąta
# pierwsza = float(input("podaj pierwszą wartość: "))
# druga = float(input("podaj drugą wartość: "))
# trzecia = float(input("podaj trzecią wartość: "))
# war1 = (pierwsza+druga)>trzecia
# war2 = (pierwsza+trzecia)>druga
# war3 = (trzecia+druga)>pierwsza
# if war1 and war2 and war3:
#     print("można zbudować trójkąt")
#     if pierwsza==druga==trzecia:
#         print("jest to trójkąt rownoboczny")
#     elif pierwsza==druga or druga==trzecia or pierwsza==trzecia:
#         print("mamy trójkąt równoramienny")
#     else:
#         print("mamy trójkąt różnoboczny")
# else:
#     print("nie można złożyć trójkąta")


# #zadanie3: złożony system logowania
# nazwa = input("podaj nazwe użytkownika: ")
# haslo = input("podaj hasło: ")
# klucz = input("podaj klucz administratora: ")

# if nazwa=='admin' and haslo=='root123' and klucz=='XYZ42':
#     print("zalogowano")
# elif nazwa=='user' and haslo=='pass123':
#     print("zalogowano jako użytkownik")
# elif nazwa=='guest' and haslo==' ':
#     print("zalogowano jako gość")
# else:
#     print("Błąd logowania")

#zadanie4:czy to data poprawna?

dzien = int(input("podaj dzień (1-31): "))
miesiac = int(input("podaj miesiąc (1-12): "))
rok = int(input("podaj rok: "))

if miesiac==(4 or 6 or 9 or 11) and 30<dzien:
    print("nie ma takiej daty")
elif miesiac==(1 or 3 or 5 or 7 or 8 or 10 or 12) and 31<dzien:
    print("też nie ma takiego dnia")
elif miesiac==2 and rok%4==0:
    if dzien > 29:
        print("znowu chujowo")
elif miesiac==2 and rok%4!=0:
    if dzien > 28:
        print("wyjątkowo chujowo, brawo")

        

