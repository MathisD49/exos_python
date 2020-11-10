from PIL import Image
from math import *

def HideImage(FirstImagePath, SecondImagePath):
    def notreImage(FirstImagePath, SecondImagePath):
        global image, image2, longueur_image, largeur_image, longueur_image2, largeur_image2
        image = Image.open(FirstImagePath) #on ouvre l'image, elle servira à récupérer les pixels
        image2 = Image.open(SecondImagePath) #on ouvre la même image pour ajouter les modification de l'image
        longueur_image, largeur_image = image.size #on récupère la longueur et la largeur de l'image
        longueur_image2, largeur_image2 = image2.size

    def pixelscolor():
        global rgb_value
        rgb_value = []
        for y in range(largeur_image):
            for x in range(longueur_image):
                r,g,b = image.getpixel((x, y))
                rgb_value.append(r)
                rgb_value.append(g)
                rgb_value.append(b)

    def putcolor(image2):
        color_image2 = []
        i = 0
        for y in range(largeur_image2):
            for x in range(longueur_image2):
                try:
                    r,g,b = image.getpixel((x, y))
                    image2.putpixel((x, y), (rgb_value[i], g, b))
                    i += 1

                except IndexError:
                    pass


    notreImage(path)
    pixelscolor()

def FindImage():
    pass

HideImage("testfinal.jpg", "testresultISN.jpg")
