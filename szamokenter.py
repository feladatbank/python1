'''
Készíts egy programot, amely a felhasználótól számokat kér be mindaddig, amíg az csupán ENTER-t nem üt! 
A számokat tárolja el a program egy listában! Az adatbekérés befejezte után írja ki a program a lista elemeit, a legkisebb és a legnagyobb számot!

'''
szamlista = []

while True:
  szamok = input("kérek egy számot:")
  if szamok != "":
    szamlista.append(szamok)
  else:
    szamlista.sort(key = int)
    print(szamlista)
    break
