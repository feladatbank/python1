'''
1.1 Feladat
Készíts egy programot, amely a felhasználótól keresztneveket kér be egészen addig, amíg az ENTER-t nem üt (nem ad meg újabb nevet a bekérésnél)! 
A program a bekért neveket írja ki a képernyőre!
'''
szavak = []
szo = None
while szo !='':
    szo = input( 'Adj meg keresztneveket! ')
    if szo != '':
        szavak.append(szo)
print(szavak)
