# ----- ZD Rozgalezenia Czesc 3 ----- #




#Zadanie 3
print("Dostepni operatorzy: OperatorA, OperatorB, OperatorC")

operator_wych = input("Podaj operatora wychodzacego: ")
operator_przych = input("Podaj operatora przychodzacego: ")
czas = float(input("Podaj czas rozmowy: "))

#Przypisanie stawek do operatorow
if operator_wych == "OperatorA":
    stawka_wych = 0.30 
elif operator_wych =="OperatorB":
    stawka_wych = 0.25
elif operator_wych == "OperatorC":
    stawka_wych = 0.40
else:
    stawka_wych = 0
    print("Nieznany operator!")

if operator_przych == "OperatorA":
    stawka_przych = 0.30


srednia_stawka = (stawka_wych + stawka_przych) / 2
koszt = round(srednia_stawka * czas, 2)
print(f"Koszt polacznia: {koszt} zl.")