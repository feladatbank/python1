'''
Írj egy programot while ciklussal, amely a felhasználótól páros számot kér be. Amennyiben a megadott szám páratlan, újra és újra megtörténik az adatbekérés mindaddig, amíg végül páros számot nem ad meg a felhasználó.
'''

while True:
  paros_szam = int(input("Adj meg egy páros számot "))
  if paros_szam % 2 == 1:
    print("A megadott szám páratlan ")
  else:
    break
