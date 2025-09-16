# Konkatenacja (laczenie)

a = "Hello"
b = "World"

c = a + " " + b
print(c)

print(len(c))

print(a[1:4])

# Metody
tekst = "witaj swiecie"
print(tekst.upper())
print(tekst.lower())
print(tekst.capitalize())
print(tekst.title())
print(tekst.replace("i","1"))
print(tekst.startswith("Witaj"))
print(tekst.endswith("cie"))
print(tekst.split(" "))
print("!".join(['A', 'B']))

# Sprawdzanie zawartosci
print("abc".isalpha())
print("123".isdigit())
print("abc123".isalnum())
print(" ".isspace())

# kodowanie
# kodowanie ASCII
print(ord('A'))
print(chr(65))

# unicode
print(ord('à'))
print(chr(10084),chr(10084),chr(10084),chr(10084),chr(10084),chr(10084),chr(10084),chr(10084))

s = "é"
b = s.encode("utf-8")
print(b)

# formatowanie stringow
imie = "Ania"
wiek = 5
print(f"{imie} ma {wiek} lat.")
print("""{} ma {}
      lat """.format(imie, wiek))

tekst = "witaj swiecie"
print(tekst.find("swiecie"))
# print(tekst.index("swiecie"))
print(tekst.count("i"))