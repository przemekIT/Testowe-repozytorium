print("1==1:", 1==1)
print("1==2:", 1==2)
print("1 !=1:", 1!=1)
print("1 !=2:", 1!=2)
car = 49
if car == 100:
    print("Speed is 100")
if car > 50 and car < 150:
    print("Car speed is between 50 km/h and 150 km/h")
else:
    print("Speed i under 50 km/h")


x = int(input("Podaj jakas wartosc: "))

if x > 0:
    print("x jest wiekszy od 0")
elif x > 5:
    print("x jest mniejszy od 5")
elif x > 10:
    print("x jest mniejszy od 10")
else:
    print("ani to ani to")
print("Koniec instrukcji")
