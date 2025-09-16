with open("tekst.txt", "r", encoding="utf-8") as text:
    ead_text = text.read()
    print(ead_text)
    print(type(ead_text))


    chaactes = []
    for cha in ead_text:
        chaactes.append(cha)
    print(len(chaactes))

    lines = ead_text.splitlines()
    print(len(lines))

    wods = ead_text.split(" ")
    print(len(wods))


# with open("tekst.txt", "w", encoding="utf-8") as text: