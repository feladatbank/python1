'''
Nagyobb szám.
A program kérjen be két számot a felhasználótól, majd írja ki, hogy melyik a nagyobb! 
A program üzeneteinek megfogalmazásában kövesse az alábbi mintát:
--------------
Adj meg egy számot! 1
Adj meg egy másik számot! 17
A nagyobb érték 17
--------------
Adj meg egy számot! 28
Adj meg egy másik számot! -2
A nagyobb érték: 28
---------------
Adj meg egy számot! 999
Adj meg egy másik számot! 999
A két szám egyenlő
------------------
'''

szam = int(input("Adj meg egy számot! "))
szam2 = int(input("Adj meg egy másik számot! "))
if szam > szam2:
    print(f"A nagyobb érték {szam}")
if szam < szam2:
    print(f"A nagyobb érték {szam2}")
if szam == szam2:
    print(f"A két szám egyenlő")
