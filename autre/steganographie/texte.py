from PIL import Image
from math import *

def HideText(texte, path):
    def strVersBinaire(texte):
        global bits
        global lenBinaire
        texteVersBinaire = []
        for char in texte:
            lettreBinaire = bin(ord(char))[2:].zfill(8) #on convertie chaques lettre en nombre puis on les converties en binaire (encodé sur 8 bits)
            texteVersBinaire.append(lettreBinaire) #on ajoute chaque lettre binaire dans la liste "texteVersBinaire"

        strBinaire = "".join(texteVersBinaire) #on convertie notre liste en chaine de caractères
        lenBinaire = len(strBinaire) #on récupère la longueur de notre chaine de caractère

        bits = []
        for i in range(0, len(strBinaire), 2):#on découpe notre chaine de caractère en chaine de 2 bits par 2 bits
            bits.append(strBinaire[i:i+2]) #on ajoute à la suite les 2 bits dans la liste "bits"



    def notreImage(path):
        global image, image2, longueur
        image = Image.open(path) #on ouvre l'image, elle servira à récupérer les pixels
        image2 = Image.open(path) #on ouvre la même image pour ajouter les modification de l'image
        longueur, largeur = image.size #on récupère la longueur et la largeur de l'image


    def uneLigne():
        global key
        for i in range(int(lenBinaire/2)):
            rougeBits = []
            r,g,b = image.getpixel((i, 0)) #on récupère la composante RGB des pixels dont on aura besoin sur la première ligne (par rapport à la longueur de la liste "bits")
            rougeBinaire = bin(r)[2:].zfill(8) #on convertie la composante rouge de chaque piels utilisés en binaire

            for y in range(0, len(rougeBinaire), 2):
                rougeBits.append(rougeBinaire[y:y+2]) #comme pour la liste "bits" on va regrouper 2 par 2 les bits contenue dans la variable "rougeBinaire" pour les ajouter à la liste "rougeBits"

            rougeBits[3] = bits[i] #On remplace le dernier bit de notre rouge par un bit de notre chaine de caractère


            strRougeBits = "".join(rougeBits) # convertir notre liste de bits en chaine de caractère et la cobvertir en nombre
            newValRouge = int(strRougeBits, 2) #on convertie notre composante rouge sous forme binaire en nombre
            key = len(bits)

            image2.putpixel((i, 0), (newValRouge, g, b)) #on ajoute la composante rouge modifié au pixel

        image2.save("u.bmp", "BMP")
        print("la clé est " + str(key))

    def plusieursLignes():
        global key
        nb = 0
        ligneY = len(bits)/(longueur)
        nbLigneUtilise = ceil(ligneY) #on arrondie la variable "ligneY" pour savoir le nombre de lignes qu'on utilisera

        for y in range(nbLigneUtilise):
            for x in range(longueur):
                rougeBits = []
                try:
                    r,g,b = image.getpixel((x, y))
                    rougeBinaire = bin(r)[2:].zfill(8)

                    for i in range(0, len(rougeBinaire), 2):
                        rougeBits.append(rougeBinaire[i:i+2])

                    rougeBits[3] = bits[nb]
                    strRougeBits = "".join(rougeBits)
                    newValRouge = int(strRougeBits, 2)
                    key = len(bits)

                    image2.putpixel((x, y), (newValRouge, g, b))
                    nb = nb+1

                except IndexError: # si jamais note programme à besoin de prendre une seul partie d'une ligne de pixel, il va passer tous les pixels dont il n'aura pas besoin
                    pass

        image2.save("p.bmp", "BMP")
        print("la clé est " + str(key))

    def launch_hide(path, text):
        strVersBinaire(text)
        notreImage(path)

        nombreDeLigne = len(bits) - longueur



        if nombreDeLigne <= 0:
            print("je rentre sur une ligne")
            uneLigne()

        else:
            print("je rentre sur plusieures lignes")
            plusieursLignes()

    launch_hide(texte, path)


def FindText(path, key):
    def notreImage(path):
        global image
        global longueur
        image = Image.open(path) #on ouvre l'image, elle servira à récupérer les pixels
        longueur, largeur = image.size #on récupère la longueur et la largeur de l'image

    def uneLigne(key):
        text = ""
        strText = ""
        lettreBin = []
        for i in range(key):
            rougeBits = []
            r,g,b = image.getpixel((i, 0)) #on récupère la composante RGB des pixels dont on aura besoin sur la première ligne (par rapport à la longueur de la liste "bits")
            rougeBinaire = bin(r)[2:].zfill(8) #on convertie la composante rouge de chaque piels utilisés en binaire

            for y in range(0, len(rougeBinaire), 2):
                rougeBits.append(rougeBinaire[y:y+2])

            strText += rougeBits[3]

        for y in range(0, len(strText), 8):
            lettreBin.append(strText[y:y+8])

        for x in range(len(lettreBin)):
            text += chr(int(lettreBin[x], 2))

        print(text)

    def plusieursLignes(key):
        x = 0
        y = 0
        textBin = ""
        lettreBin = []
        text = ""
        for i in range(key):
            rougeBits = []
            r,g,b = image.getpixel((x, y))
            rougeBinaire = bin(r)[2:].zfill(8)

            for a in range(0, len(rougeBinaire), 2):
                rougeBits.append(rougeBinaire[a:a+2])

            textBin += rougeBits[3]
            x += 1

            if x == longueur:
                x = 0
                y += 1
            else:
                pass

        for y in range(0, len(textBin), 8):
            lettreBin.append(textBin[y:y+8])

        for x in range(len(lettreBin)):
            text += chr(int(lettreBin[x], 2))

        print(text)

    def launch_find(path, key):
        notreImage(path)

        if key <= longueur:
            uneLigne(key)

        else:
            plusieursLignes(key)

    launch_find(path, key)
