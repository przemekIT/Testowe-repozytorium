# Zadanie 1
a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
c = float(input("Podaj trzecią liczbę: "))
print("Suma:", a+b+c)
print("Iloczyn:", a*b*c)

# Zadanie 2
pensja = int(input("Ile wynosi twoja pensja? "))
rata = int(input("Ile wynosi twoja rata? "))
komuna = int(input("Ile wynosi zapłata za usługi komunalne? "))
zysk = pensja - (rata + komuna)
print(f"Zarobiłeś {zysk} zł.")

# Zadanie 3
przekatna1 = float(input("Podaj długość pierwszej przekątnej: "))
przekatna2 = float(input("Podaj długość drugiej przekątnej: "))
pole_rombu = przekatna1 * przekatna2 / 2
print("Pole rombu wynosi ", pole_rombu)
print(type(pole_rombu))

# Zadanie 4
print("Być", "albo", "nie być.", sep="\n")

# Zadanie 5
print('"Życie jest tym,' \
'\n' + ' ' * 3 + 'co dzieje się,' \
'\n' + ' ' * 7 + 'gdy jesteś zajęty robieniem innych planów."' \
'\n' + ' ' * 11 + '~ John Lennon')