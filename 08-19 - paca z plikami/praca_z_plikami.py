# Pliki tekstowe - .txt, .csv, .json - zapisane jako ciągi znaków
# Pliki binarne - .jpg, .png, .mp3, .exe - dane zapisywane w postaci bajtów


# open(nazwa_pliku, tryb, encoding)
# "r" - odczyt (read), plik musi istnieć
# "W" - zapis (write), tworzy nowy plik lub nadpisuje istniejący
# "a" - dopisanie (append), dopisuje na końcu pliku
# "X" - tworzy nowy plik, błąd jeśli plik istnieje
# "b" - tryb binarny ("rb", "wb")
# "t" - tryb tekstowy, domyslny

# # Pierwsza metoda do otwierania pliku
# plik = open('dane.txt', "r", encoding="utf-8")
# zawartosc = plik.read()
# print(zawartosc)
# plik.close()

# # Druga, bezpieczniejsza i lepsza metoda do pracy z plikami
# with open('dane.txt', "r", encoding="utf-8") as plik:
#     zawartosc = plik.read()
#     print(zawartosc)


# # read()
# with open('dane.txt', "r", encoding="utf-8") as plik:
#     print(plik.read())

# # readline()
# with open('dane.txt', "r", encoding="utf-8") as plik:
#     print(plik.readline())
#     print(plik.readline())
#     print(plik.readline())

# # readlines()
# with open('dane.txt', "r", encoding="utf-8") as plik:
#     lines = plik.readlines()
#     for line in lines:
#         print(line)

# # iteracja
# with open('dane.txt', "r", encoding="utf-8") as plik:
#     for linia in plik:
#         print(linia.strip())


# # Write
# with open("output.txt", "w", encoding="utf-8") as f:
#     f.write("Hello, world!\n")
#     f.write("Druga linia\n")

# # writelines()
# linie = ["Linia1\n", "Linia2\n", "Linia3\n"]
# with open("output.txt", "w", encoding="utf-8") as f:
#     f.writelines()

# # dopisywanie do pliku
# with open("output.txt", "a", encoding="utf-8") as f:
#     f.write("Nowa linia na końcu\n")

# with open("Python-logo.png", "rb") as f:
#     dane = f.read()

# with open("kopia.jpg", "wb") as f:
#     f.write(dane)

# try:
#     with open("nieistniejacy.txt", "r", encoding = "utf-8") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("Plik nie istnieje!")

# import os

# print(os.getcwd()) 
# print(os.listdir("."))
# # os.rename("dane.txt", "nowe_dane.txt")
# # os.remove("nowe_dane.txt")
# os.mkdir("nowy_folder")

# from pathlib import Path

# sciezka = Path("kopia.jpg")

# print(sciezka.exists())
# print(sciezka.is_file())
# print(sciezka.suffix)

# import csv

# with open("dane.csv", "w", encoding = "utf-8") as f:
#     writer = csv.writer(f, delimiter=";")
#     writer.writerow(["Imię", "Wiek"])
#     writer.writerow(["Anna", 25])

# with open("dane.csv", "r", encoding="utf-8") as f:
#     reader = csv.reader(f, delimiter=";")
#     for wiersz in reader:
#         print(wiersz)

# import json

# dane = {"imie": "Anna", "wiek": 25}

# with open("dane.json", "w", encoding="utf-8") as f:
#     json.dump(dane, f, indent=10)

# with open("dane.json", "r", encoding="utf-8") as f:
#     odczyt = json.load(f)
#     print(odczyt)

# Zadanie 6 - import shutil, shutil.copy(plik, sciezka/plik)
# Zadanie 5 - from collections import Counter