'''
Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot, és ezeket tárolja el egy listában! 
A program adja össze a lista elemeit, írja ki a képernyőre az összegüket és a lista elemeit!
'''
import random
szamok = []
for i in range(5):
    szamok.append(random.randint(1, 10))
print(f"A lista elemei: {szamok}")
print(f"a lista összege: {sum(szamok)}")
