from carre import Carre

class CarreTest:
    def __init__(self):
        pass

    def test(self):
        carre1 = Carre(2)
        carre2 = Carre(6)

        print(carre1.perimeter == 8)
        print(carre1.area == 4)
        print(carre1.factor(2) == 4)
        print(carre1.addition(carre2) == 8)
        print(carre1.soustraction(carre2) == -4)
        print(carre1.integer() == 2)
        print(carre1.inferieur(carre2) == True)
        print(carre1.superieur(carre2) == False)
        print(carre1.inferieur_egal(carre2) == True)
        print(carre1.superieur_egal(carre2) == False)
        print(carre1.egal(carre2) == False)
        print(carre1.different(carre2) == True)

a = CarreTest()
print(a.test())

#facultatif
