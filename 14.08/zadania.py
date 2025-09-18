#zadanie1
try:
    a = float(input("Podaj pierwszą liczbę: ").replace(',', '.'))
    b = float(input("Podaj drugą liczbę: ").replace(',', '.'))
    wynik = a / b
    print(f"Wynik: {wynik}")
except ZeroDivisionError:
    print("Błąd: nie można dzielić przez zero.")
except ValueError:
    print("Błąd: podaj poprawne liczby.")

#zadanie2
#1) wewnątrz funkcji
def podziel_v2(a, b):
    try:
        print(f"Wynik: {a/b}")
    except ZeroDivisionError:
        print("Błąd: nie można dzielić przez zero.")
    except (TypeError, ValueError):
        print("Błąd: podaj poprawne liczby.")

a = input("a: ").replace(',', '.')
b = input("b: ").replace(',', '.')
podziel_v2(a if a else 0, b if b else 0)  # możesz też rzutować przed wywołaniem: podziel_v2(float(a), float(b))

#2) na  zewnątrz
def podziel_v1(a, b):
    print(f"Wynik: {a/b}")

try:
    a = float(input("a: ").replace(',', '.'))
    b = float(input("b: ").replace(',', '.'))
    podziel_v1(a, b)
except ZeroDivisionError:
    print("Błąd: nie można dzielić przez zero.")
except ValueError:
    print("Błąd: podaj poprawne liczby.")

#zadanie4
#1) Wyjątek obsługiwany na zewnątrz
def konwersja_v1(s: str):
    x = float(s.replace(',', '.'))   # brak try/except w funkcji
    print(f"Wynik: {x}")

txt = input("Podaj wartość: ")
try:
    konwersja_v1(txt)
except ValueError:
    print("Błąd: nie da się przekonwertować na liczbę.")

#2) Wyjątek obsługiwany wewnątrz funkcji
def konwersja_v2(s: str):
    try:
        x = float(s.replace(',', '.'))
        print(f"Wynik: {x}")
    except ValueError:
        print("Błąd: nie da się przekonwertować na liczbę.")

txt = input("Podaj wartość: ")
konwersja_v2(txt)

#zadanie3
s = input("Podaj wartość: ")

try:
    x = float(s.strip().replace(',', '.'))
    print(f"OK -> {x}  (typ: {type(x).__name__})")
except ValueError:
    print("Błąd: nie da się przekonwertować na liczbę.")

#zadanie1-Walidator listy operacji matematycznych
def calculate_operations(operations):
    wyniki = []
    dozwolone = {"+", "-", "*", "/"}

    for krotka in operations:
        if len(krotka) != 3:
            wyniki.append("Błąd: nieprawidłowe dane wejściowe")
            continue

        a, op, b = krotka

        if op not in dozwolone:
            wyniki.append("Błąd: nieznany operator")
            continue
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            wyniki.append("Błąd: nieprawidłowy typ danych")
            continue
        if op == "/" and b == 0:
            wyniki.append("Błąd: dzielenie przez zero")
            continue

        if op == "+":   wyniki.append(a + b)
        elif op == "-": wyniki.append(a - b)
        elif op == "*": wyniki.append(a * b)
        else:           wyniki.append(a / b)

    return wyniki

ops = [(2, "+", 3), (5, "/", 0), ("a", "*", 3), (10, "^^", 2)]
print(calculate_operations(ops))
# [5, 'Błąd: dzielenie przez zero', 'Błąd: nieprawidłowy typ danych', 'Błąd: nieznany operator']