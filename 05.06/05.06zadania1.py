# Modul rozgalezenian czesc 1
#Zadanie 1

nombre = int(input("Entrez un nombre : "))

# Vérifie si le nombre est pair ou impair
if nombre % 2 == 0:
    print("pair")
else:
    print("impair")

# Zadanie 2
nombre = int(input("Entrez un nombre : "))

# Vérifie si le nombre est un multiple de 7
if nombre % 7 == 0:
    print("C'est un multiple de 7")
else:
    print("Ce n'est pas un multiple de 7")

# Zadanie 3
nombre1 = int(input("Entrez le premier nombre : "))
nombre2 = int(input("Entrez le deuxième nombre : "))

# Trouve et affiche le maximum
if nombre1 > nombre2:
    print("Le plus grand nombre est :", nombre1)
elif nombre2 > nombre1:
    print("Le plus grand nombre est :", nombre2)
else:
    print("Les deux nombres sont égaux :", nombre1)

#Zadanie 4
nombre1 = int(input("Entrez le premier nombre : "))
nombre2 = int(input("Entrez le deuxième nombre : "))

# Trouve et affiche le minimum
if nombre1 < nombre2:
    print("Le plus petit nombre est :", nombre1)
elif nombre2 < nombre1:
    print("Le plus petit nombre est :", nombre2)
else:
    print("Les deux nombres sont égaux :", nombre1)

# Zadanie 5
a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))

# Propose un choix à l'utilisateur
print("Que voulez-vous faire ?")
print("1 - Afficher la somme, la différence et le produit")
print("2 - Afficher la moyenne arithmétique")
choix = input("Entrez 1 ou 2 : ")

# Traite le choix
if choix == "1":
    print("Somme :", a + b)
    print("Différence :", a - b)
    print("Produit :", a * b)
elif choix == "2":
    moyenne = (a + b) / 2
    print("Moyenne arithmétique :", moyenne)
else:
    print("Choix invalide.")