seats = {"A1": None, "A2": None, "A3": None, "B1": None}

class SeatTakenError(Exception):
    pass

def reserve_seat(seats, seat_code):
    try:
        if seat_code not in seats:
            raise ValueError("Nie ma takiego miejsca!")
        if seats[seat_code] == "X":
            raise SeatTakenError("Miejsce juz zajęte!")
        seats[seat_code] = "X"
        return f"Miejsce {seat_code} zostało zarezerwowane."
    except ValueError as e:
        return f"Błąd: {e}"
    except SeatTakenError as e:
        return f"Błąd: {e}"

seats = {"A1": None, "A2": None, "A3": None, "B1": None}
   
print(reserve_seat(seats, "A1"))
print(reserve_seat(seats, "A1"))
print(reserve_seat(seats, "Z9"))

