#1
"""def maFonction(a):
    return a*5

print(maFonction(5))"""

#2
"""def maFonction(liste):
    pairs = []
    for i in range(len(liste)):
        if liste[i]%2 == 0:
            pairs.append(liste[i])
        else:
            pass
    return pairs

a = [1, 2, 3, 4, 5, 6]
print(maFonction(a))"""

#3
"""def maFonction(n):
    f = [0, 1]
    for i in range(2, n+1):
        fn = f[i-1] + f[i-2]
        f.append(fn)

    return f

a = maFonction(8)
print(a)"""

#4
"""def fonctionFor(chaine):
    nbvoyelle = 0
    voyelle = ["a", "e", "i", "o", "u", "y"]
    for i in range(len(chaine)):
        for k in range(len(voyelle)):
            if chaine[i] == voyelle[k]:
                nbvoyelle += 1
            else:
                pass

    return nbvoyelle

def fonctionWhile(chaine):
    nbvoyelle = 0
    nb = 0
    voyelle = ["a", "e", "i", "o", "u", "y"]
    while nb != len(chaine):
        nbv = 0
        while nbv != len(voyelle):
            if chaine[nb] == voyelle[nbv]:
                nbvoyelle += 1
                nbv += 1
            else:
                nbv += 1
        nb += 1
    return nbvoyelle

def maFonction(chaine):
    nbvoyelle = 0
    voyelle = ["a", "e", "i", "o", "u", "y"]
    for i in range(len(chaine)):
        if chaine[i] in voyelle:
            nbvoyelle += 1

    return nbvoyelle"""

#5
"""def factorielle(n):
    resultat = 1
    for i in range(1, n+1):
        resultat *= i

    return resultat

print(factorielle(10))"""

#6
"""def factorielle(n):
    if n < 2:
        return n
    else:
        return n * factorielle(n-1)

print(factorielle(10))"""

#7
"""def somme(*n):
    nbargument = 0
    nb = 0
    for i in n:
        nbargument += 1
        nb += i

    return str(nb) + " avec " + str(nbargument) + " arguments"

print(somme(1, 3, 5, 8))"""

#8
def maFonction(liste):
    chiffre = []
    for i in liste:
        if i <= 9:
            chiffre.append(i)
        else:
            i = str(i)
            chiffre.append(int(i[0]))

    return chiffre

def autreFonction(chiffre):
    resultat = {}
    for k in range(len(chiffre)):
        if k != 0:
            b = {str(k): chiffre.count(k)}
            resultat.update(b)

    return resultat

a = [1, 4 ,9 ,16 ,25 ,36 ,49 ,64 ,100 ,121]
print(autreFonction(maFonction(a)))
