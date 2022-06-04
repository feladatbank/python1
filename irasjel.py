#Készíts egy programot, amely a felhasználó által megadott mondatról a mondatvégi jel alapján eldönti milyen fajtájú! (kijelentő, kérdő, felkiáltó / felszólító / óhajtó)
#Lehetséges megoldás

mondat = input("Írj le egy mondatot mondatvégi írásjellel ")
if mondat[-1] =="!":
  print("Ez egy felkiáltó / felszólító / óhajtó mondat ")
if mondat[-1] == ".":
  print("Ez egy kijelentő mondat ")
if mondat[-1] == "?":
  print("Ez egy kérdő mondat ")
