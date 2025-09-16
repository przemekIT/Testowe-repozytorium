# # Zad 1
# kraje = {'Polska', 'Włochy', 'Ukraina', 'Turcja', 'Norwegia'}
# print(kraje)

# def dodaj():
#     dodaj_kraj = input("Jaki kraj chcesz dodać?: ")
#     kraje.add(dodaj_kraj)
#     print(kraje)

# def usun():
#     usun_kraj = input("Jaki kraj chcesz usunąć?: ")
#     kraje.remove(usun_kraj)
#     print(kraje)

# def wyszukaj():
#     wyszukaj_kraj = input("Jaki kraj chcesz wyszukać?: ").capitalize()
#     for kraj in kraje:
#         if kraj.startswith(wyszukaj_kraj):
#             print(kraj)
    
# def czy_zawiera():
#     czy_jest = input("Jaki kraj sprawdzasz?: ").capitalize()
#     if czy_jest in kraje:
#         print(f"Tak! {czy_jest} jest w tym zbiorze.")
#     else:
#         print(f"Niestety nie ma {czy_jest} w tym zbiorze.")

# while True:
#     print('''
# 0 - Wyjdź
# 1 - Dodaj kraj
# 2 - Usuń kraj
# 3 - Wyszukaj kraj (po pierwszych znakach)
# 4 - Sprawdź czy jest taki kraj''')
#     opcja = int(input(": "))

#     if opcja == 0:
#         break
#     elif opcja == 1:
#         dodaj()
#     elif opcja == 2:
#         usun()
#     elif opcja == 3:
#         wyszukaj()
#     elif opcja == 4:
#         czy_zawiera()

# Zad 2
miasta1 = {'Kraków', 'Warszawa', 'Łódź', 'Katowice'}
miasta2 = {'Szczecin', 'Suwałki', 'Gdynia', 'Zakopane', 'Kraków'}

miasta3 = {miasto for miasto in miasta1 if miasto in miasta2}
# print(miasta3)

# Zad 3
miasta1 = {'Kraków', 'Warszawa', 'Łódź', 'Katowice'}
miasta2 = {'Szczecin', 'Suwałki', 'Gdynia', 'Zakopane', 'Kraków'}

miasta3 = {miasto for miasto in miasta1 if miasto not in miasta2}
# print(miasta3)

# Zad 4
miasta1 = {'Kraków', 'Warszawa', 'Łódź', 'Katowice'}
miasta2 = {'Szczecin', 'Suwałki', 'Gdynia', 'Zakopane', 'Kraków'}

miasta3 = {miasto for miasto in miasta2 if miasto not in miasta1}
# print(miasta3)

# Zad 5
miasta1 = {'Kraków', 'Warszawa', 'Łódź', 'Katowice'}
miasta2 = {'Szczecin', 'Suwałki', 'Gdynia', 'Zakopane', 'Kraków'}

miasta3 = {miasto for miasto in miasta1 if miasto not in miasta2}
for miasto in miasta2:
    if miasto not in miasta1:
        miasta3.add(miasto)
# print(miasta3)

# Zad 6
kraj_stolica = {
    "Polska": "Warszawa",
    "Niemcy": "Berlin"
    }

print(kraj_stolica)

def dodaj(kraj, stolica):
    kraj_stolica[kraj] = kraj_stolica.get(kraj, stolica)

def usun(kraj):
    kraj_stolica.pop(kraj)

def wyszukaj(kraj):
    print(kraj_stolica.get(kraj))

def zastap(kraj, nowa_stolica):
    kraj_stolica.update({kraj: nowa_stolica})

dodaj("Francja", "Paryż")
print(kraj_stolica)

usun("Polska")
print(kraj_stolica)

wyszukaj("Niemcy")

zastap("Niemcy", "Frankfurt")
print(kraj_stolica)