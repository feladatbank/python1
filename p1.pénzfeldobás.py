'''
A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását (fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e!
'''

from random import choice

lista = ['fej', 'irás']

beker = input('Fej vagy írás?: ')
valaszt = choice(lista)

if beker == valaszt:
    print('Eltaláltad')
else:
    print('nem találtad el')
