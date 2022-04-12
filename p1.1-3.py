"""
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal! Az összehasonlítás eredményéről tájékoztassa a felhasználót!
"""

import random

lista = [1, 2, 3]

randomszam = int(input("Írj be egy számot: "))
szam = random.choice(lista)
print(szam)

if szam > randomszam:
  print("A beírt szám kisebb!")
if szam < randomszam:
  print("A beírt szám nagyobb!")
if szam == randomszam:
  print("A beírt szám egyenlő!")
