# producenci = ("BMW", "Audi", "Toyota", "BMW", "Mercedes", "BMW", "Audi")

# print("Aktualna krotka producentów:", producenci)

# szukany = input("Podaj nazwę producenta do zastąpienia: ")
# zastepnik = input("Podaj słowo zastępcze: ")

# producenci_lista = list(producenci)
# for i in range(len(producenci_lista)):
#     if producenci_lista[i] == szukany: 
#         producenci_lista[i] = zastepnik

# producenci = tuple(producenci_lista)

# print("Zaktualizowana krotka producentów: ", producenci)

# samochody=("Opel", "Volkswagen", "Opel", "Fiat", "Citroen", "Lamborgini", "Citroen", "Peugot")

# lista_samochodow=list(samochody)
# # print(lista_samochodow)
# nazwa_producenta=input("Podaj nazwe producenta samochodow, ktorego chcesz zamienic ? ")
# nazwa_nowa=input("Podaj nazwe marki na jaka chcesz podmienic?")

# for i, samochod in enumerate(lista_samochodow):
#     if samochod==nazwa_producenta:
#         lista_samochodow[i]=nazwa_nowa
#         break



# print(lista_samochodow)


def tuple_item_replace(tup_lst: tuple, word: str, replace_str: str):
    return tuple([replace_str if s == word else s for s in tup_lst])