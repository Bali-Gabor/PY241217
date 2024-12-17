# 1.feladat

# Feladat: Szövegfeldolgozás és listaműveletek
# Bemenet:
# Kérj be egy mondatot a felhasználótól!
# A mondat szavai legyenek szóközökkel elválasztva.
# Feladatok:
# a) Írd ki a mondat összes szavát egy listában!
# b) Tedd a listában szereplő szavakat fordított sorrendben egy másik listába, és írd ki!
# (Tehát az utolsó szó kerüljön előre, az első pedig hátra.)
# c) Alakítsd át a mondatot úgy, hogy minden szó nagybetűvel kezdődjön!
# (A többi betű maradjon kisbetű.)
# d) Ellenőrizd, hogy szerepel-e a mondatban egy megadott szó (pl. "alma")! Írd ki az eredményt (van/nincs)!
# e) Számold meg, hány szó szerepel a mondatban, és írd ki!
# Kimenet: A programnak ki kell írnia a fenti részfeladatok eredményeit a konzolra.


# from moduls import *

# mondat=input('Írjon be egy mondatot!  ')

# uj_mondat=alakit(mondat)
# print(uj_mondat)
# print(fordit(uj_mondat))
# print(nagy(uj_mondat))
# valasz=input('Milyen szót keresel a mondatban?  ')
# keres(valasz, uj_mondat)
# print(f'A mondatban {len(uj_mondat)} szó van.')



# 2. feladat

# Új Feladat: Szöveg Elemzése és Manipulációja
# Ebben a feladatban tovább gyakorolhatod a stringek és listák kezelését, miközben szövegeken dolgozol.

# Feladat leírása:
# Bemenet:

# Kérj be a felhasználótól egy szöveget, amely több mondatból áll. A mondatokat pont (.) választja el egymástól.
# Feladatok:

# a) Tördeld fel a szöveget mondatokra, és tárold ezeket egy listában.
# b) Írd ki, hogy hány mondat van a szövegben!
# c) Kérd be a felhasználótól egy kulcsszót, majd keresd meg, hogy hány mondat tartalmazza ezt a szót.
# d) Tedd a mondatokat fordított sorrendbe, majd írd ki a szöveget újra a fordított mondatsorrenddel.
# e) Alakítsd át a szöveget úgy, hogy minden mondat nagybetűvel kezdődjön.
# Kimenet: A programnak ki kell írnia a fenti részfeladatok eredményeit a konzolra.

# from moduls import *

# valasz=input('Írj be egy szöveget!  ')

# print(mondat(valasz))
# print(f'A szöveg {len(mondat(valasz))} mondatból áll.')

# szo=input('Adj meg egy keresendő szót!  ')

# print(f'A lista {keres (szo, mondat(valasz))} mondatában szerepel a(z) {szo} szó.')
# print(fordit(mondat(valasz)))
# print(nagy(mondat(valasz)))





