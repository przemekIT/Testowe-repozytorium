# https://materials.itstep.org/content/af94b5e3-5e8b-4156-9d33-07240d7846a9/pl
# Zadanie 1
try:
    liczba = float(input("Podaj liczbę: "))

    if liczba < 0:
        raise ValueError("Podano liczbę ujemną!")

    wynik = 100 / liczba
    print(f"Iloraz 100 / {liczba} = {wynik}")

except ValueError as e:
        print(f"Błąd: {e}")
except ZeroDivisionError:
    print("Błąd: Dzielenie przez zero jest niemożliwe!")


# Zadanie 2


# Zadanie 3,4
def list_menu():
    num_list = []
    while True:
        try:
            user_input = input("Podaj liczbę do listy (puste aby zakończyć): ")
            if user_input == "":
                break
            num_list.append(int(user_input))
        except Exception as e:
            print("Error:", e)
 
    while True:
        print('-'*10)
        print("Menu")
        print("1. Wyświetl listę")
        print("2. Max wartość")
        print("3. Min wartość")
        print("4. Element wg indeksu")
        print("5. Usuń według indeksu")
        print("0. Wyjście")
 
        try:
            option = int(input("Podaj opcję: "))
            if option == 0:
                break
            elif option == 1:
                print(num_list)
            elif option == 2:
                print(max(num_list))
            elif option == 3:
                print(min(num_list))
            elif option == 4:
                index = int(input("Wyświetl- Podaj index: "))
                print(num_list[index])
            elif option == 5:
                index = int(input("Usuń - Podaj index: "))
                num_list.pop(index)
            else:
                print("Błędna opcja")
        except IndexError as e:
            print("Zły indeks")
        except Exception as e:
            print("Error:", e)
 
 
 
def list_menu_2():
    num_list = []
    while True:
        user_input = input("Podaj liczbę do listy (puste aby zakończyć): ")
        if user_input == "":
            break
        num_list.append(int(user_input))
 
    while True:
        print('-'*10)
        print("Menu")
        print("1. Wyświetl listę")
        print("2. Max wartość")
        print("3. Min wartość")
        print("4. Element wg indeksu")
        print("5. Usuń według indeksu")
        print("0. Wyjście")
 
        option = int(input("Podaj opcję: "))
        if option == 0:
            break
        elif option == 1:
            print(num_list)
        elif option == 2:
            print(max(num_list))
        elif option == 3:
            print(min(num_list))
        elif option == 4:
            index = int(input("Wyświetl- Podaj index: "))
            print(num_list[index])
        elif option == 5:
            index = int(input("Usuń - Podaj index: "))
            num_list.pop(index)
        else:
            print("Błędna opcja")
 
 
list_menu()
 
try:
    list_menu_2()
except IndexError as e:
    print("Zły indeks")
except Exception as e:
    print("Error:", e)
 