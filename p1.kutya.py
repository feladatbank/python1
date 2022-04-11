'''
Írj egy programot, amely a felhasználótól bekéri egy kutya nevét, életkorát, fajtáját, és azt hogy rendelkezik-e érvényes oltással veszettség ellen! 
Az adatokat tárolja a program szótárban, és írja ki a képernyőre az adatszerkezetet!
'''
nev = input('kutya neve: ')
faj = input('kutya fajtája: ')
kor = int(input('kutya kora: '))
olt = input('a kutya oltott-e? (i/n) : ')

szotar = {
    'nev' : nev ,
    'faj' : faj,
    'kor': kor,
    'oltott_e': olt
    }

print(szotar)
