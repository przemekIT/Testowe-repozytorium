if True:
    print("warunek spełniony")

if False:
    print("Warunek spełniony")      #kod się nigdy nie wykona bo mamy false który zawsze ma wartość logiczną 0

wiek = 19
if wiek >= 18:
    print("Jesteś osobą pełnoletnią!")
    print("masz więcej niż 18 lat")

print("2 == 2:", 2==2)
print("1 == 2:", 1==2)
print("2 != 2:", 2!=2)
print("1 != 2:", 1!=2)
print("2 > 2:", 2>2)
print("1 > 2:", 1>2)
print("2 <= 2:", 2<=2)

#Jakie wartości są zastępowane przez false
if "":
    print("pusty ciąg")

#operacje logiczne
if True and True:
    print("jebac")

if 0 and False:
    print("jebac jebac")

if 2 or False:
    print("jebac jebac")

if "" or False:
    print("jebac jebac")

adult = False
if not adult:
    print("pieprzony gówniarz")

time = int(input("Enter the current time in hours: ")) %24
ticket = False
money = True
luggage = False
print(money or ticket and not luggage and time>6)

print(False or True and True)

car_speed = 200
motorcycle_speed = 150

if car_speed == 100:
    print("Prędkość jest 100")


if car_speed >50 and car_speed <150:
    print("Car speed is between 50 km/h and 150 km/h")
else:
    print("Prędkość nie jest w przedziale 50-150")


if car_speed > motorcycle_speed:
    print("chuj")

#elif
# car_speed = 100
# motorcycle_speed = 100

if car_speed > motorcycle_speed:
    print("Car is faster than motorcycle")
    motorcycle_speed += 50
elif motorcycle_speed > car_speed:
    print("Motorcycle is faster than car")
    motorcycle_speed += 50
else:
    print("Car and motorcycle are equally fast")
    motorcycle_speed +=50


x = int(input("podaj wartość:"))
if x>0:
    print("x jest większy od 0")
elif x > 5:
    print("x jest większy od 5")
else:
    print("ani to ani to")


#ostatni przykład
account = int(input("Enter how much you put: "))
account = abs(account)

if account > 0:
    withdrawal = int(input("Enter how much you take: "))
    withdrawal = abs(withdrawal)                                #abs=wartość bezwzględna
    if withdrawal < account:
        account -= withdrawal
        print("Here are your", withdrawal, ".")
        print("There are", account, "left.")
    else:
        print("There are only", account, ".")
else:
    print("There are no money in piggy bank")