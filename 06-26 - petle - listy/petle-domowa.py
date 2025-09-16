# Liczby wypełnione gwiazdkami
while True:
    print("Wpisz tekst, używając liter od 'a' do 'j'.")
    print("Jeśli chcesz zakończyć program wpisz: '0'.")
    text = input("Wpisz tekst: ").lower()

    height = 15
    width = 30

    if text == "0":
        break

    for letter in text:

        if letter == "a":
            space_count = 0
            star_count = width

            for j in range(height):
                print(" "*space_count + "*"*star_count, end="")
                
                star_count -= width // height
                space_count += width // height

                print()
                
        elif letter == "b":
            space_count = width
            star_count = 0

            for j in range(height):
                print(" "*space_count + "*"*star_count, end="")
                
                space_count -= width // height
                star_count += width // height

                print()
                
        elif letter == "c":
            space_count = 0
            star_count = width

            for j in range(height):
                print(" "*space_count + "*"*star_count + " "*space_count, end="")
                
                star_count -= ((width // height) * 2)
                space_count += width // height

                print()

        elif letter == "d":
            space_count = width
            star_count = -width

            for j in range(height + 1):
                print(" "*space_count + "*"*star_count + " "*space_count, end="")
                
                star_count += ((width // height) * 2)
                space_count -= width // height

                print()

        elif letter == "e":
            space_count = 0
            star_count = width

            for j in range(height):
                print(" "*space_count + "*"*star_count + " "*space_count, end="")
                
                if j < (height // 2):
                    star_count -= ((width // height) * 2)
                    space_count += width // height
                else:
                    star_count += ((width // height) * 2)
                    space_count -= width // height

                print()

        elif letter == "f":
            space_count = width
            star_count = 0

            for j in range(height):
                print("*"*star_count + " "*space_count + "*"*star_count, end="")
                
                if j < (height // 2):
                    space_count -= ((width // height) * 2)
                    star_count += width // height
                else:
                    space_count += ((width // height) * 2)
                    star_count -= width // height

                print()

        elif letter == "g":
            space_count = width
            star_count = 0

            for j in range(height):
                print("*"*star_count + " "*space_count, end="")
                
                if j < (height // 2):
                    space_count -= ((width // height) * 2)
                    star_count += width // height
                else:
                    space_count += ((width // height) * 2)
                    star_count -= width // height

                print()

        elif letter == "h":
            space_count = width
            star_count = 0

            for j in range(height):
                print(" "*space_count + "*"*star_count, end="")
                
                if j < (height // 2):
                    space_count -= (width // height)
                    star_count += width // height
                else:
                    space_count += (width // height)
                    star_count -= width // height

                print()

        elif letter == "i":
            space_count = 0
            star_count = width

            for j in range(height):
                print("*"*star_count + " "*space_count, end="")
                
                star_count -= width // height
                space_count += width // height

                print()

        elif letter == "j":
            space_count = width
            star_count = 0

            for j in range(height):
                print(" "*space_count + "*"*star_count, end="")
                
                space_count -= width // height
                star_count += width // height

                print()

        else:
            continue
