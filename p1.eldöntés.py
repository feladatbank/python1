'''
Írj egy programot, amely 5 darab véletlenszámot generál [1;7] intervallumon,
és ezeket eltárolja egy listában. Kérjen be a felhasználótól egy számot,
és vizsgálja meg, hogy ez előfordul-e a listában! Az eredményről tájékoztassa a felhasználót,
és írja ki a lista elemeit a képernyőre!

Pld:
Kérek egy számot: 1
A megadott szam megtalalhato a listaban, [4, 2, 1, 2, 3]
'''
from random  import randint
lista=[]
for i in range(5):
    lista.append(randint(1,7))

beker = int(input('Kérek egy számot: '))

if beker in lista:
    print(f'a megadott szam megtalalhato a listaban, {lista}')
else:
    print("A megadott szam nem talalhato a listaban")

