#A program tároljon egy listában színeket. Kérjen be a felhasználótól egy színt, és állapítsa meg, hogy a megadott szín már szerepel-e az adott listában. 
#Lehetséges megoldás

szinek = ['citromsárga', 'piros', 'fehér', 'fekete', 'zöld', 'narancssárga', 'piros', 'lila', 'kék']

szin = input('Adj meg egy színt!\t')
if szin in szinek:
	print('A megadott szín szerepel a listában.')
else:
	print('A megadott szín nem szerepel a listában.')

print('A lista színei:')
for szin in szinek:
	print(szin, end=', ')
