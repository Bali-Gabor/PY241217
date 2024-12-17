# 1. feladat


# def alakit(a:str)->list[str]:
#     lista=a.split(' ')
#     return lista


# def fordit(a:list)->list[str]:
#     return a[::-1]


# def nagy(a:list):
#     for szo in a:
#         print(szo.capitalize(), end=' ')
#     print(' ')


# def keres(a:str, b:list):
#     if a in b: print('A szó benne van a mondatban.')
#     else: print('A szó nincs benne a mondatban.')


# 2. feladat


# def mondat(valasz:str)->list[str]:
#     lista = valasz.split('.')
#     lista.pop()
#     return lista


# def keres(szo:str, lista:list[str])->int:
#     darab=0
#     for mondat in lista:
#         if szo in mondat: darab+=1
#     return darab

# def fordit(lista:list[str])->list[str]:
#     return lista[::-1]


# def nagy(lista:list[str])->list[str]:
#     return '. '.join([mondat.capitalize() for mondat in lista])+'.'
