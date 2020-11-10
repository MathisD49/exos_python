class Carre:
    count = 0
    def __init__(self, cote):
        self.cote = cote
        self.perimeter = self.perimeter()
        self.area = self.area()
        Carre.count += 1
        self.phrase = "Le carré à un côté d'une longueur de ", self.cote, "cm, une aire de ", self.area, "cm2 et un périmètre de ", self.perimeter, "cm"


    def perimeter(self):
        return self.cote * 4

    def area(self):
        return self.cote ** 2

    def factor(self, x):
        a = Carre(x*self.cote)
        return a.cote

    def __add__(self, carre1):
        cote_carre = self.cote
        cote_carre1 = carre1.cote

        return Carre(cote_carre + cote_carre1)

    def __sub__(self, carre1):
        cote_carre = self.cote
        cote_carre1 = carre1.cote

        return Carre(cote_carre - cote_carre1)

    def integer(self):
        return int(self.cote)

    def __lt__(self, carre1):
        a = self.cote
        b = carre1.cote
        return a < b

    def __gt__(self, carre1):
        a = self.cote
        b = carre1.cote
        return a > b

    def __le__(self, carre1):
        a = self.cote
        b = carre1.cote
        return a <= b

    def __ge__(self, carre1):
        a = self.cote
        b = carre1.cote
        return a >= b

    def __eq__(self, carre1):
        a = self.cote
        b = carre1.cote
        return a == b

    def __ne__(self, carre1):
        a = self.cote
        b = carre1.cote
        return a != b


if __name__ == "__main__":
    a = Carre(8)
    b = Carre(5)
    c = a + b
    print(c.perimeter)
    #print(a.integer())
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
