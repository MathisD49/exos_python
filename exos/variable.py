#1
"""nombre = 12
print(nombre)"""

#2
"""age, prenom = 18, "mathis"
phrase = "Je suis " + prenom + " et j'ai " + str(age) + " ans"
print(phrase)"""

#4
"""nombre = 4
print(nombre*5)"""

#5
"""nombre = 5
print(nombre)
nombre = nombre + 1
print(nombre)
nombre += 1
print(nombre)"""

#6
"""nombre = 5
print(nombre)
nombre = nombre - 1
print(nombre)
nombre -= 1
print(nombre)"""

#7
"""nombre = 5
print(nombre)
nombre = nombre * 2
print(nombre)
nombre *= 2
print(nombre)"""

#8
"""nombre = 5
print(nombre)
nombre = nombre / 2
print(nombre)
nombre /= 2
print(nombre)"""

#9
"""a = 1
b = 2
a, b = b, a"""

#10
"""a = 1
b = 1

a = b = 1

a, b = 1, 1"""

#11
"""a = 10
print(a)
print(a/2)
print(a//2)
print(a%2)
print(a**3)"""

#12
"""prixHT = float(input("entrez le prix : "))
nbarticle = float(input("entrez le nombre d'article : "))
TVA = 1.2
prixTTC = prixHT*nbarticle*TVA
print(prixTTC)"""

#13
"""liste = [4, 5]
print(liste)"""

#14
"""liste = ["salut", "toi", 4, 5]
print(liste)
print(liste[0])
print(type(liste[2]))"""

#15
"""x = [10, 12]
y = [24, 50]
z = x + y
print(z)"""

#16
"""x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(x[3])
print(x[3:5])
print(x[2:7:2])
print(len(x))
print(min(x))
print(max(x))
print(sum(x))
del(x[3:5])
print(x)"""

#17
"""x = ["ok", 4, 2, 78, "bonjour"]
print(x[3])
x[1] = "toto"
print(x)"""

#18
"""x = [0, 1, 2, 3, 4, 5]
print(x)

z = []
for i in range(6):
    z += [i]

print(z)"""

#19
"""x = {"key": "valeur", "key2": "valeur2"}
print(x)

print(x["key"])

a = {"titi": "toto"}
x.update(a)

x["titi"] = "tata"

print(x)

del x["titi"]

x["key"] = ""
print(x["key"])

print(x)

y = {}
y.update(x)
print(y)"""

#20
"""x = [(1, 2), (3, 4), (5, 6), (7, 8)]

print(x)

x.append("a")
print(x)

x += "b"
print(x)

y = ["1", "2", "3"]
x += y
print(x)

x.insert(4, "2")
print(x)

print(y)

z = y
print(z)

y = []
print(y)

del z[:]
print(z)"""
