class Carre:
    count = 0
    def __init__(self, cote):
        self.cote = cote
        self.perimeter = self.perimeter()
        self.area = self.area()
        Carre.count += 1


    def perimeter(self):
        return self.cote * 4

    def area(self):
        return self.cote ** 2

    def factor(self, x):
        a = Carre(x*self.cote)
        return a

    def addition(self, carre1):
        a = carre.cote
        b = carre1.cote
        return Carre(a+b)

    def soustraction(self, carre1):
        a = carre.cote
        b = carre1.cote
        return Carre(a-b)

    def inferieur(self, carre1):
        a = carre.cote
        b = carre1.cote
        return a < b

    def superieur(self, carre1):
        a = carre.cote
        b = carre1.cote
        return a > b

    def inferieur_egal(self, carre1):
        a = carre.cote
        b = carre1.cote
        return a <= b

    def superieur_egal(self, carre1):
        a = carre.cote
        b = carre1.cote
        return a >= b

    def egal(self, carre1):
        a = carre.cote
        b = carre1.cote
        return a == b

    def different(self, carre1):
        a = carre.cote
        b = carre1.cote
        return a != b


if __name__ == "__main__":
    #a = Carre(5)
    #print(a.count)
    #b = Carre(3)
    #print(a.count)
    #print(carre.different(carre1))
    #carre_final = carre.soustraction(carre1)
    #print(carre_final.cote)

    #print(carre.perimeter)
    #print(carre.factor(5))
    #print(carre.area)
    #print("Le carré à un côté d'une longueur de ", carre.cote, "cm, une aire de ", carre.area, "cm2 et un périmètre de ", carre.perimeter, "cm")
