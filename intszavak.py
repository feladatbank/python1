"""
írj egy programot, ami: bekér egy számot (int), majd egy tetszőleges karakterláncot (string). 
Ezt követően kiírja a karakterláncot csupa nagybetűvel, egymás mellé, szóközökkel elválasztva annyiszor, amennyiszer a bekért egész szám volt!"""

"""
Minta: (output)

1.feladat:
írj be egy egész számot: 12
írj be egy tetszőleges szöveget: hörcsög
HÖRCSÖG HÖRCSÖG HÖRCSÖG HÖRCSÖG HÖRCSÖG HÖRCSÖG HÖRCSÖG HÖRCSÖG HÖRCSÖG HÖRCSÖG HÖRCSÖG HÖRCSÖG 

"""

# lehetséges megoldás

print("1.feladat:")
bekeres = int(input("írj be egy egész számot: "))
bekeres2 = input("írj be egy tetszőleges szöveget: ")
bekeres2 = bekeres2.upper()
for i in range(bekeres):
  print(bekeres2, end=" ")
