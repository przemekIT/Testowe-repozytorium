# # Zadanie 1 - moja
# while True:
#     x = input("Podaj liczbę: ")

#     if x.isdigit():
#         int(x)
#     else:
#         print("Nie podałeś liczby!")
#         continue

#     print("Wybierz jedną z opcji:")
#     print("0 - zakończ")
#     print("1 - ile cyfr ma liczba")
#     print("2 - podaj sumę wszystkich cyfr liczby")
#     print("3 - podaj średnią wszystkich cyfr liczby")
#     print("4 - ile zer ma liczba")
    
#     opcja = input(": ")

#     if opcja == "0":
#         break

#     elif opcja == "1":
#         count = 0
#         for i in x:
#             count += 1
#         print(f"Liczba ma tyle cyfr: {count}")

#     elif opcja == "2":
#         count = 0
#         for i in x:
#             count += int(i)
#         print("Suma wszystkich cyfr wynosi:", count)

#     elif opcja == "3":
#         count_num = 0
#         count_i = 0
#         for i in x:
#             count_i += 1
#             count_num += int(i)
#         print("Średnia wszystkich cyfr wynosi:", count_num/count_i)

#     elif opcja == "4":
#         count_zero = 0
#         for i in x:
#             if i == "0":
#                 count_zero += 1
#         print("Liczba ma tyle zer:", count_zero)

#     else:
#         print("Błędna komenda.")

# # Zadanie 1 / A - Przemka
# print("Podaj liczbę do analizy.")
# liczba = input("Wpisz liczbę: ")
 
# suma = 0
# ile_cyfr = 0
# ile_zer = 0
 
# for znak in liczba:
#     if znak.isdigit():
#         cyfra = int(znak)
#         suma += cyfra
#         ile_cyfr += 1
#         if cyfra == 0:
#             ile_zer += 1
 
# if ile_cyfr > 0:
#     srednia = suma / ile_cyfr
# else:
#     srednia = 0
 
# print("Liczba cyfr: ", ile_cyfr)
# print("Suma cyfr: ", suma)
# print("Średnia cyfr: ", srednia)
# print("Liczba zer: ", ile_zer)


# # Zadanie 2 - szachownica
# X = int(input("Podaj rozmiar komórek:"))

# for i in range(4):
#     print("")
#     print("*"*X, "_"*X, sep="", end="")
#     print("*"*X, "_"*X, sep="", end="")
#     print("*"*X, "_"*X, sep="", end="")
#     print("*"*X, "_"*X, sep="", end="")
#     print("")
#     print("_"*X, "*"*X, sep="", end="")
#     print("_"*X, "*"*X, sep="", end="")
#     print("_"*X, "*"*X, sep="", end="")
#     print("_"*X, "*"*X, sep="", end="")


# # Zadanie 3
# import random
 
# print("Wybierz poziom trudności: ")
# print("1. Łatwy (1-5)")
# print("2. Średni (1-10)")
# print("3. Trudny (1-20)")
 
# poziom = int(input("Wybór: "))
# ile_pytan = 5
# punkty = 0
 
# if poziom == 1:
#     max_liczba = 5
# elif poziom == 2:
#     max_liczba = 10
# else:
#     max_liczba = 20
 
# i = 0
# while i < ile_pytan:
#     a = random.randint(1, max_liczba)
#     b = random.randint(1, max_liczba)
 
#     print("Ile to:", a, "*", b, "?")
#     odp = int(input("Odpowiedź:"))
 
#     if odp == a * b:
#         print("Dobrze!")
#         punkty += 1
#     else:
#         print("Źle! Poprawna odpowiedź to: ", a * b)
 
#     i += 1
 
# print("Twoje punkty:", punkty, "punkty /", ile_pytan, "pytań")


# # Zadanie 4 - romb
# a = int(input("Podaj długość rombu (liczba nieparzysta): "))
# b = int(input("Podaj wysokość rombu (liczba nieparzysta): "))

# srodek_dlugosci = (a-1)/2
# srodek_szerokosci = (b-1)/2

# for i in range(b):
#     for j in range(a):
#         if (j == srodek_dlugosci - i) or (j == srodek_dlugosci + i):
#             print("*", end="")
#         elif (j == i - srodek_dlugosci) or (j == i + srodek_dlugosci):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# for i in range(b):
#     for j in range(a):
#         if j == srodek_wysokosci:
#             print("*", end="")
#         elif i == srodek_dlugosci:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()



