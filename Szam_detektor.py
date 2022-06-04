"""
Közepes
3.- Szám detektor: a felhasználotól kérjen be egy szöveget (string formában) 
és ezután egy program menjen végig és néze meg egyesével hogy van e a szövegben szám (int) ha van akkor tegye be azt egy külön listába.
"""

lista = []

felhasz = input("Kérek egy szöveget számmal és szavakkal: ").strip(" ")

for i in felhasz:
    try:
        int(i)
    except:
        pass
    else:
        lista.append(i)

print(lista)
