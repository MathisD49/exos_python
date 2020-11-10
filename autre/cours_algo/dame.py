#tableau = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

class dame:
    def __init__(self):
        self.creation = self.creationJeuDame()

    def creationJeuDame(self):
        tab = []
        for i in range(0, 10):
            for j in range(0, 10):
                tab.append([i, j])
        return tab

    def dameBlanc(self, tableau):
        blanc = {}
        nb = 0
        for i in range(0, 40, 2):
            if tableau[i][0]%2 == 0:
                blanc[str(nb)] = tableau[i]
            else:
                blanc[str(nb)] = tableau[i+1]
            nb += 1

        return blanc

    def dameNoir(self, tableau):
        noir = {}
        nb = 0
        for i in range(99, 60, -2):
            if tableau[i][0]%2 == 0:
                noir[str(nb)] = tableau[i]
            else:
                noir[str(nb)] = tableau[i-1]
            nb += 1

        return noir

if __name__ == "__main__":
    a = dame()
    b = a.creation

    ligne = int(input("entrez le numéro de la ligne de votre case : "))
    colonne = int(input("entrez le numéro de la colonne de votre case : "))
    coordonnee = [ligne, colonne]

    if coordonnee in a.dameBlanc(b).values():
        key_pion = 0
        for i,j in a.dameBlanc(b).items():
            if j == coordonnee:
                key_pion = i

        print("--------------------")
        print("0 - en haut à gauche")
        print("1 - en haut à droite")
        print("2 - en bas à gauche")
        print("3 - en bas à droite")
        print("--------------------")
        deplacement = int(input("où voulez vous mettre votre pion : "))
        print(a.dameBlanc(b))


        if deplacement == 0:
            a.dameBlanc[str(key_pion)] = [coordonnee[0]+1, coordonnee[1]-1]
            print(a.dameBlanc(b))
        elif deplacement == 1:
            a.dameBlanc[str(key_pion)] = [coordonnee[0]+1, coordonnee[1]+1]
            print(a.dameBlanc(b))
        elif deplacement == 2:
            a.dameBlanc[str(key_pion)] = [coordonnee[0]-1, coordonnee[1]+1]
            print(a.dameBlanc(b))
        elif deplacement == 3:
            a.dameBlanc[str(key_pion)] = [coordonnee[0]-1, coordonnee[1]+1]
            print(a.dameBlanc(b))
        else:
            print("mauvaise entrée")
    else:
        print("il n'y a pas de pion")



























"""ligne = int(input("entrez le numéro de la ligne de votre case : "))
colonne = int(input("entrez le numéro de la colonne de votre case : "))

if ligne < 0 or ligne > 9:
    print("mauvaise entrée")
    quit()

if colonne < 0 or colonne > 9:
    print("mauvaise entrée")
    quit()"""
