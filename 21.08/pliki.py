# https://itsteppledu.sharepoint.com/sites/PythonWtCzw22052025/Shared%20Documents/General/Pliki%20(2).pdf
# Start od Zadanie 3
# Zadanie 3
# with open("tekst.txt", "r", encoding="utf-8") as plik:
#     linie = plik.readlines()

# with open("bez_pustych.txt", "w", encoding="utf-8") as nowy:
#     for linia in linie:
#         if linia.strip():   # sprawdzamy czy linia nie jest pusta
#             nowy.write(linia)

# print("Plik został zapisany jako 'bez_pustych.txt' bez pustych linii.")

# Zadanie 8
from datetime import datetime
import time

def log(komunikat):
    czas = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{czas}] {komunikat}\n")

def pokaz_logi():
    with open("log.txt", "r", encoding="utf-8") as f:
        for linia in f:
            print(linia.strip())

# przyklad uzycia

log("Uzytkownik uruchomil program")

# akcja, gdzie uruchamiamy funkcje odpowiedzialna za uruchomienie programu

time.sleep(5)

log("Uzytkownik dodaje teraz notatke")
# uzytkownik, dodaje notatke