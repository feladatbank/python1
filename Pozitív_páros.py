'''
1. Feladat
Készíts egy programot, amely a felhasználótól bekér egy egész számot, majd megvizsgálja, hogy a megadott szám
- pozitív páros vagy
- negatív páratlan.
Az eredményről tájékoztatja a felhasználót.
Pld:
------------------------
Kérek egy számot: 2
Pozitív páros.
------------------------
Kérek egy számot: -1
Negatív páratlan.
'''

#megoldás:
beker = int(input('Kérek egy számot: '))
if beker > 0 and beker %2 == 0:
    print('Pozitív páros.')
if beker < 0 and beker %2 != 0:
    print('Negatív páratlan.')
