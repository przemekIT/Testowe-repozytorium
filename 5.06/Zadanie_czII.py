# # #zadanie1
# x= float(input("Enter the number: "))
# if x%2==0:
#     print("parzysta")
# else:
#     print("nieparzysta")

# # #zadanie2
# y= float(input("Enter the number: "))
# if y%7==0:
#     print(y, "Twoja liczba jest wieloktro..")
# else:
#     print(y, "nie jest")

# #zadanie3
# a= float(input("Enter the number: "))
# b= float(input("Enter the number: "))

# if a>b:                                     #możemy to zrobić funkcją max -> print(max(a,b))
#     print(a)
# elif a<b:
#     print(b)

# #zadanie4
# c= float(input("Enter the number: "))
# d= float(input("Enter the number: "))
# if c>d:
#     print(d)
# elif c<d:
#     print(c)                                #możemy to zrobić funkcją min -> print(min(a,b))

# #zadanie5
# e= float(input("Enter the number: "))
# f= float(input("Enter the number: "))
# suma=e+f
# różnica=e-f
# iloczyn=e*f
# iloraz=e/f
# średnia=(e+f)/2
# operacja=(input("Choose your operation: "))
# if operacja=='suma':
#     print(suma)
# elif operacja =='różnica':
#     print(różnica)
# elif operacja =='iloczyn':
#     print(iloczyn)
# elif operacja =='iloraz':
#     print(iloraz)
# elif operacja =='średnia':
#     print(średnia)

#Część 2

#zadanie1
czas = int(input("podaj czas w sekundach od początku dnia: "))
do_północy = 86400 - czas
po_konwersji = do_północy//3600 
print(po_konwersji, "godzin", (do_północy)//60, "minut", (do_północy)%60, "sekund")

#wersja Przema zad1
seconds_since_midnight = int(input("podaj czas w sekundach od początku dnia: "))
total_seconds_in_day = 24 * 60 * 60
remaining_seconds = total_seconds_in_day - seconds_since_midnight
hours = remaining_seconds // 3600
minutes = (remaining_seconds % 3600) // 60
seconds = remaining_seconds % 60

print(f"Do północy pozostało: {hours} godzin, {minutes} minut oraz {seconds} sekund.")

#zadanie2
średnica = float(input("podaj średnicę okręgu: "))
pole = 3.14 * (średnica/2)^2
obwód = 2*średnica
operacja = input("jakaoperacja: ")
if operacja == 'pole':
    print("wynik pola to: ", pole)
elif operacja == 'obwód':
    print("wynik obwodu to: ", obwód)
else:
    print("nieznana operacja")

#wersja Przema zad2.
import math
diamater = float((input("podaj średnicę okręgu: ")))
choice = input("wpisz 'pole' aby obliczyć pole lub 'obwód' aby obliczyć obwód okręgu")
radius = diamater/2
if choice == 'pole':
    area = math.pi * radius **2
    print(f"Pole okręgu jest równe {area:.2f}")
elif choice == 'obwód':
    circumference = 2*math.pi * radius
    print(f"Obwód okręgu jest równy {circumference:.2f}")
else:
    print("Nieprawidłowy wybór")

#zadanie3
koszt_konsoli = float(input("podaj koszt jednej konsoli: "))
ilość =  int(input("ile tych konsol: "))
rabat = float(input("jaki rabat: "))

koszt_zamówienia = koszt_konsoli*ilość*rabat
rabat_jedna_konsola = rabat*koszt_konsoli

operacja(input("co chcesz wiedzieć: "))
if operacja == 'koszt_zamówienia':
    print(koszt_zamówienia)
elif operacja == 'rabat_jedna_konsola':
    print(rabat_jedna_konsola)
else:
    print("nie przewidziano operacji")

#wersja Przema zad3.
price = float(input("podaj cene jednej konsoli:"))
quantity = int(input("podaj ilość konsol: "))
discount = float(input("podaj rabat w procentach np. 10 dla 10%: "))
choice = input("wpisz 'całość' aby obliczyć całkowitą kwotę lub 'jedna' aby obliczyć koszt jednej po rabacie: " )

discounted_price = price*(1-discount/100)

if choice == 'całość':
    total = discounted_price * quantity
    print(f"Całkowita kwota zamówienia: {total:.2f} zł")
elif choice == 'jedna':
    print(f"koszt jednej konsoli po rabacie: {discounted_price:.2f} zł")
else:
    print("nieprawidłowy wybór")


#zadanie4
size_of_data = float(input("podaj rozmiar pliku w gigabajtach: "))
przepustowość = float(input("podaj przepustowość łącza w bitach na sekunde: "))

#wersja Przema zad4.
file_size_gb = float((input("podaj rozmiar pliku w GB: ")))
bandwidth_bps = float(input("podaj przepustowość łącza w bitach na sekundę: "))
choice = input("wybierz jednostkę czasu: 'godziny', 'mminuty' lub 'sekundy': ")

#1GB = 8 * 10^9 bitów (1 bajt = 8 bitów, 1GB = 10^9)
file_size_bits = file_size_gb * 8 * 1_000_000_000
download_time_seconds = file_size_bits / bandwidth_bps

if choice == 'sekundy':
    print(f"Czas pobierania: {download_time_seconds:.2f} sekund")
elif choice == "minuty":
    print(f"Czas pobierania: {download_time_seconds/60:2f} minut")
elif choice == 'godzin':
    print(f"Czas pobierania: {download_time_seconds/3600:2f} godzin")
else:
    print("Nieprawidłowy wybór")


#zadanie5
godzina = input("podaj godzinę od  ")

#wersja Przema zad5.
hour = int(input("Podaj godzinę (0-23): "))

if 0 <= hour < 6:
    print("good night")
elif 6 <= hour < 13:
    print("Good morning")
elif 17 <= hour < 24:
    print(("good evening"))
else:
    print("Nieprawidlowa godzina")

