# https://itsteppledu.sharepoint.com/sites/PythonWtCzw22052025/Shared%20Documents/General/Wyjatki%20zadania.pdf
# Zadanie 1


# Zadanie 2
def reserve_seat(seats, seat_code):
    # sprawdzenie czy miejsce istnieje
    if seat_code not in seats:
        raise ValueError(f"Miejsce {seat_code} nie istnieje.")

    # sprawdzenie czy miejsce jest wolne (None oznacza brak miejsca, X oznacza zajęte)
    if seats[seat_code] == "X":
        raise (f"Miejsce {seat_code} jest już zajęte.")

    # rezerwacja miejsca
    seats[seat_code] = "X"
    print(f"Miejsce {seat_code} zostało zarezerwowane.")

# Zadanie 4
def parse_json_like(string):
    try:
        result = eval(string)
        if isinstance(result, dict):
            return result
        else:
            return "Błąd: niepoprawny format"
    except (SyntaxError, NameError):
        return "Błąd: niepoprawny format"

# --- Przykład użycia ---
print(parse_json_like("{'key': 'value'}")) 
print(parse_json_like("{'key': 'value',"))
print(parse_json_like("[1, 2, 3]"))        
       