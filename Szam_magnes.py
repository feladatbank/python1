"""
Nagyon Könnyű
1.- Szám mágnes: egy számsorozatból meg kell álapitanod hogy van e benne egy felhaszálotól bekért szám 
(pl: 43810927473216892133632417713519261001162821015129167066013316395100090512329)
"""



szam = str(438109274732168921336324177135192610011628210151291670660133163951000905123299)

felhasz_szam = int(input("Kérek egy számot 0-9 közöt: "))

darab = 0

for i in szam:
    if int(i) == felhasz_szam:
        darab += 1

print(darab)