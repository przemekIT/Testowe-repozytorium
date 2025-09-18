# 1.literały liczbowe
x=10
y=2
z=50
print(x)
print(type(x))  #type wyswietla typ tej zmiennej

# 2.literały zmiennoprzecinkowe (float)
    
a= 3.14
b= -0.0001
print(type(a))

# 3. complex
print(z.real)
print(z.imag)
print(type(z))

# 4.literały tekstowe
txt1 = "Ala"
txt2 = "ma kota"
txt3 = txt1 + txt2

print(txt3)
print(type(txt1))
print(txt1, txt2, sep=' ')

# 5.literały logiczne
x = True
y = False

var1 = 5
var2 = 5

print(y)
print(5>3)
print(2==5)
print(2 is 5)

print(var1 == var2)
print(var1 is var2) #za pomocą 'is' sprawdzamy referencję do obiektu. te adresy w pamięci powinny być różne i powinno być niby False.

# 6. literał pusty
x=None
print(id(x))
print(type(x))
print(x)

print('I like "Monty Python"')