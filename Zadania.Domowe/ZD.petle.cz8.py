# Zadanie 1
while True:
    print("Wybierz liczbę do wydrukowania z gwiazdek:")
    print("1. Jeden")
    print("2. Dwa")
    print("3. Trzy")
    print("4. Cztery")
    print("5. Piec")
    print("0. Wyjście")

    wybor = input("Wpisz swój wybór (0-5): ")

    if wybor == "1":
        print("   *")
        print("   *")
        print("   *")
    elif wybor == "2":
        print(" ***")
        print("   *")
        print(" ***")
        print("*   ")
        print("****")
    elif wybor == "3":
        print(" ***")
        print("   *")
        print(" ***")
        print("   *")
        print(" ***")
    elif wybor == "4":
        print("*  *")
        print("*  *")
        print("****")
        print("   *")
        print("   *")
    elif wybor == "5":
        print("****")
        print("*   ")
        print("****")
        print("   *")
        print("****")    
    elif wybor == "0":
        print("Do widzenia!")
        break
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
