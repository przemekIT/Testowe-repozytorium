ksiazka1 = {"fantasy", "przygodowa", "młodzieżowa"}
ksiazka2 = {"fantasy", "epicka", "dla_dorosłych"}
 
 
print("Tagi wspólne: ", ksiazka1 & ksiazka2)
print("Tagi unikatowe dla książki 1", ksiazka1 - ksiazka2)
print("Tagi unikatowe dla książki 2", ksiazka2 - ksiazka1)
print("Wszystkie tagi:", ksiazka1 | ksiazka2)