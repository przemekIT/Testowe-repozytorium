# tekst = input("Podaj liczbę: ")
 
# try:
#     liczba = int(tekst)
#     print("Podana liczba to:", liczba)
# except ValueError:
#     print("Błąd: Podany ciąg znaków nie jest liczbą")


# # wariant 1
# def konwertuj_bez_obslugi(tekst):
#     liczba = float(tekst)
#     print("Wprowadzona liczba to: ", liczba)

# try:
#     dane = input("Podaj liczbę: ")
#     konwertuj_bez_obslugi(dane)
# except ValueError:
#     print("Błąd: nie mona przekonwertować podanego tekstu na liczbe")


# # wariant 2
# def konwertuj_z_obsluga(tekst):
#     try:
#         liczba = float(tekst)
#         print("Wprowadzona liczba to: ", liczba)
#     except ValueError:
#         print("Błąd: nie mona przekonwertować podanego tekstu na liczbę")


# dane = input("Podaj liczbę")
# konwertuj_z_obsluga(dane)

# def print_division(a, b):
#     try:
#         if b == 0:
#             raise ZeroDivisionError("Nie dziel przez zero")
#         print(a/b)
#     except ZeroDivisionError:
#         print("Nie dzielimy przez 0")
 
# def print_division_2(a, b):
#     if b == 0:
#         raise ZeroDivisionError("Nie dziel przez 0")
#     print(a/b)
    
 
# a = int(input("Pierwsza liczba: "))
# b = int(input("Druga liczba: "))
# print_division(a, b)
 
# try:
#     print_division_2(a, b)
# except Exception as e:
#     print(f"Błąd: {e}")
 


# ZADANIE 3,4 
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