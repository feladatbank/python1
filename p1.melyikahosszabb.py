'''
Szavak.
A program kérjen be két szót a felhasználótól, majd írja ki, hogy melyik a hosszabb! 
A program üzeneteinek megfogalmazásában kövesse az alábbi mintát:
-----
Adj meg egy szót! kelkáposzta
Adj meg egy másik szót! kisegér
A hosszabb szó: kelkáposzta
---- 
Adj meg egy szót! kelkáposzta
Adj meg egy másik szót! káposztafej
A két szó egyforma hosszú.
----- 
Adj meg egy szót! árvíztűrő
Adj meg egy másik szót! tükörfúrógép
A hosszabb szó: tükörfúrógép
'''

szo = input("Adj meg egy szót! ")

szo2 =  input("Adj meg egy másik szót! ")

if len(szo) > len(szo2):
    print(f"A hosszabb szó:{szo}")
if len(szo) < len(szo2):
    print(f"A hosszabb szó:{szo2}")
if len(szo) == len(szo2):
    print(f"A két szó egyforma hosszú.")
