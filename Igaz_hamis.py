"""
Nehéz
4.- Igaz/Hamis: a program kérjen be egy számot 1 és 10 között ezután a program probálja ki találni a megadott választ. 
minden alkalommal a program tippel egy számra 1 és 10 közöt és a felhasználonak igaz, hamissal kell válaszolnia a megfelellő helyzetben
a program addig menjen amedig a program ki nem találja. 
Ha a felhasználó csak aka.: Igazat mond ha a felhasználotól bekért szám nem egyezik meg a random számmal amit a program add meg vagy fordítva akkor a felhasználó veszit
"""
import random

felhasz_szam = int(input("Kérek egy számot 1 és 10 között: "))

while True:
    program_talal = random.randint(1,10)
    print(program_talal)
    
    iga_ham = input("adja meg hogy a program eltalálta e vagy sem (True / False): ").lower()

    if felhasz_szam == program_talal and iga_ham in "true":
        print("Program: YAY :D")
        break

    if felhasz_szam == program_talal and iga_ham in "false":
        print("Program: HEH! Pedig tudom hogy jó! TE CSALÓ >:(")
        break
    
    if felhasz_szam != program_talal and iga_ham in "false":
        print("Program: Oh ")
    
    if felhasz_szam != program_talal and iga_ham in "true":
        print("Program: Heh miért hazudsz amikor tudom hogy nem az :( ")


     



