# Zadanie 1
tekst = input("Wpisz ciąg znaków: ")

if tekst == tekst[::-1]:
    print("To jest palindrom.")
else:
    print("To nie jest palindrom.")

# Zadanie 2
tekst = input("Wpisz tekst: ")
zastrzezone = input("Wpisz zastrzeżone słowa (oddzielone spacją): ")

slowa = tekst.split()
nowy_tekst = ""
for slowo in slowa:
    if slowo.lower() in zastrzezone.split():
        nowy_tekst += slowo.upper() + " "
    else:
        nowy_tekst += slowo + " "

print("Zmodyfikowany tekst:")
print(nowy_tekst.strip())

# Zadanie 3
text = input("Wpisz text gdzie wyrazy sa podzielone kropka: ")
ilosc_zdan = 0

for x in text:
    if x in ".?!":
        ilosc_zdan += 1
print(f"Ilosc zdan to: {ilosc_zdan}")