def replace_char(file, replacement: str, replacer: str):
    with open(file, "r") as f:
        data = f.read()
        data = data.replace(replacement, replacer)

    with open(file, "w") as f:
        f.write(data)

    print("Text replaced")


replace_char('przeplyw.txt', ',', '.')