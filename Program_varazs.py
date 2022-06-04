"""
Könnyű
2.- Program varázs: egy program kérjen be 3 számot, ezután a program döntse el hogy: 
melyik a leg kisseb, 
melyik a legnagyobb 
és hogy van e benne páros.
"""
lista = []

for i in range(3):
    felhasz_szam = int(input("Kérek egy számot: "))
    lista.append(felhasz_szam)

kissebb = min(lista)
nagyobb = max(lista)

for y in lista:
    if y % 2 == 0:
        valasz = "van benne páros"
    else:
        valasz = "nincs benne páros"

print(f"{kissebb}, {nagyobb} és {valasz}.")
