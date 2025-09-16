# Zadanie 1
text = input("Podaj tekst, a sprawdzę czy jest palindromem: ")

split_text = text.split()
joined_text = ""

for word in split_text:
    for letter in word:
        if letter.isalpha():
            joined_text += letter

if joined_text.lower() == joined_text[::-1].lower():
    print("To palindrom!")
else:
    print("To nie palindrom :(")


# Zadanie 2
# text = "Ala ma kota, ale czy kot ma Alę? Dowiemy się kiedy indziej."
# reserved = ["Ala", "kot", "ale"]
text = input("Podaj tekst: ")
reserved_text = input("Wypisz słowa zarezerwowane, oddzielone ', ' przecinkiem i spacją: ")
reserved = reserved_text.split(", ")

split_text = text.split()
joined_text = ""

for word in split_text:
    if word in reserved:
        joined_text += word.upper() + " "
    else:
        joined_text += word + " "

print(joined_text)


# Zadanie 3
text = "Ala ma kota. Kot ma Alę. Nie wiem co tu bredzę. Fajną masz tu halę."

split_text = text.split(". ")
print(split_text)

print("W tekście wystąpiło tyle zdań:", len(split_text))