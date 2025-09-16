# # 1 Lista zakupow
# lista_zakupow = ['jabłko', 'banan', 'mleko', 'paluszki', 'jablko', 'brzoskwinia']
 
# def dodaj(produkt):
#     if produkt not in lista_zakupow:
#         lista_zakupow.append(produkt)
#     else:
#         print(f"{produkt} już jest na liście.")
 
# def usun(produkt):
#     if produkt in lista_zakupow:
#         lista_zakupow.remove(produkt)
#     else:
#         print(f"{produkt} nie ma na liście.")
 
# def zamien(produkt, nowy_produkt):
#     if produkt in lista_zakupow and nowy_produkt not in lista_zakupow:
#         lista_zakupow[lista_zakupow.index(produkt)] = nowy_produkt
#     else:
#         print("Nie można wykonać akcji.")
 
# def wyswietl_sort():
#     lista_zakupow.sort(key = lambda x: x[0].lower())
#     print(lista_zakupow) 
 
# dodaj('kefir')
# usun('mleko')
# zamien('jabłko', 'cytryna')
# # wyswietl_sort()
 
# def dodaj_ilosc(produkt, ilosc):
#     if produkt in lista_zakupow:
#         lista_zakupow[lista_zakupow.index(produkt)] = [produkt, f"{ilosc} kg"]
 
# dodaj_ilosc('banan', 2)
# dodaj_ilosc('jablko', 5)
# dodaj_ilosc('brzoskwinia', 10)
 
# # wyswietl_sort()
# print(lista_zakupow)
# wyswietl_sort()

lista_zakupow=['Mydlo','Balsam','Recznik','Woda','Ksiazka']
 
def usun_z_listy(zakup):
    lista_zakupow.remove(zakup)

usun_z_listy('Balsam')
