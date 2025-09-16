def dodaj_notatke(tresc):
    with open("notatki.txt", "a", encoding="utf-8") as f:
        f.write(tresc + "\n")
    
def pokaz_notatki():
    try:
        with open("notatki.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("Brak notatek.")
    
def wyczysc_notatki():
    open("notatki.txt", "w", encoding="utf-8").close()
    print("Notatki usunięte!")


pokaz_notatki()
dodaj_notatke("Pierwsza notatka w trzeciej lini")

wyczysc_notatki()
