from datetime import datetime
import time

def log(komunikat):
    czas = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{czas}] {komunikat}\n")

def pokaz_logi():
    with open("log.txt", "r", encoding="utf-8") as f:
        for linia in f:
            print(linia.strip())


# przykład uzycia

log("Uzytkownik uruchomil program")
# akcja, gdzie uruchamiamy funkcje odpowiedzialna za uruchomienie programu

time.sleep(5)

log("Uytkownik dodaje teraz notatkę")
# uzytkownik, dodaje notatkę
    