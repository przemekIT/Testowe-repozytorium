# filter bierze pod uwagę argumenty, które w funkcji zwracają True


def is_whitespace(x: str):
    for char in x:
        return char != " "
    
tekst = "Mam małą Polskę w zasięgu ręki."

# print(list(is_whitespace(tekst)))
print(str(filter(is_whitespace, tekst)))