'''
Írj egy programot while vagy for ciklussal amely kiírja a páros számokat 1 és 10 között!
'''

#while

szam = 0
while szam < 10:
  szam = szam + 2
  print(szam)

#for

for i in range(11):
    if i %2 == 0:
        print(i)
