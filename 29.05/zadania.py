#zadanie1
print("nothing", "will work", "unless you do", sep='\n')
#zadanie2
print("\"Anyone who")
print(" " * 1 + "stops")
print(" " * 3 + "learning is old,")
print(" " * 5 + "whether at twenty or eighty\"")
print(" " * 12 + "Henry Rord")
#zadanie3
x = float(input("Provide number one:"))
y = float(input("Provide number two:"))
print("Multiplying is:",x*y, "adding is:", x+y, "and cutting is:", x-y)
#zadanie4
x = float(input("Provide value:"))
y = float(input("Provide percent to calculate:"))
result = (x*y)/100
print(f"{y}% z {x} to {result}.")
# lub
print("{}% z {} to {}.".format(y,x,result))

#zadanie5
a = float(input("Provide heigh:"))
h = float(input("Provide weight:"))
z=a*h
print("Area this figure is:", z)

#zadanie3
num1 = float(input("enter your first number:"))
num2 = float(input("enter your second number:"))
dodawanie = num1+num2
odejmowanie = num1-num2
dzielenie = num1/num2
mnożenie = num1*num2
print("suma= ", dodawanie,"różnica= ",odejmowanie,"iloczyn= ", mnożenie, "iloraz= ",dzielenie, sep='\n')

#zadanie4
x = float(input("Provide number of minutes:"))
sek = x*60
print("our new value", sek)

#zadanie5
uro = int(input("podaj chuju rok narodzin:"))
latka = 2025 - uro
print("masz lat ", latka)