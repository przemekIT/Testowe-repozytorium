#----- Zadnaie 1 -----#
l = int(input("Wpisz liczbe szesciocyfrowa: "))

if 100000 <= l <= 999999:
     #Rozbijamy na cyfry
     c1 = l // 100000 % 10
     c2 = l // 10000 % 10
     c3 = l // 1000 % 10
     c4 = l // 100 % 10
     c5 = l // 10 % 10
     c6 = l % 10

     first_sum = c1 + c2 + c3
     second_sum = c4 + c5 + c6

#     if first_sum == second_sum:
#             print("TO szczesliwa liczba")
#     else:
#             print("To nie jest szczesliwa liczba")
#  print("Blad: to nie jest liczba szczesliwa.")

#----- Zadanie 3 -----#
miesiac = int(input("Wpisz jaki miesiac(od 1 do 12): "))
if miesiac == "1" or "2" or "12":
    print("Zimaaaa")
elif miesiac == min("3") and max("5"):
    print("Wiosnaaa")
elif miesiac == min("8") and max("8"):
    print("Latoooo")
elif miesiac == min("9") and max("11"):
    print("Jesien")
else:
    print("Blaaaad")
