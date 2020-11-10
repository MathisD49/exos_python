tableau1 = [3, 6, 8, 12, 58, 43, 7, 5, 6, 9, 25, 58, 37, 8, 45, 42, 72, 58, 23, 2]
tableau2 = [1, 45, 12, 2, 5, 8, 45, 87, 72, 62, 3, 6, 8, 6, 54, 56, 25, 20, 56, 4]

def fonctionDeTri(tableau):
    triTableau= []
    triTableau.append(0)
    nb = 0
    count = 0

    for i in range(len(tableau)):
        if tableau[i] >= triTableau[nb]:
            triTableau.append(tableau[i])
            count += 1
        else:
            k = 0
            for y in range(len(triTableau)):
                count += 1
                if tableau[i] < triTableau[y]:
                    triTableau.insert(y, tableau[i])
                    break

        nb += 1
    del(triTableau[0])
    print(tableau)
    print(triTableau)
    print(count)


def fonctionDeTriPlusieursTableaux(tableau1, tableau2):
    triTableau = []
    triTableau.append(0)
    nb = 0
    count = 0
    for i in range(len(tableau1)):
        if tableau1[i] >= triTableau[nb]:
            triTableau.append(tableau1[i])
        else:
            k = 0
            for y in range(len(triTableau)):
                if tableau1[i] < triTableau[y]:
                    triTableau.insert(y, tableau1[i])
                    break
        nb += 1
        count += 1

    del(triTableau[0])


    nb = 0

    for y in range(len(tableau2)):
        if tableau2[y] <= triTableau[nb]:
            triTableau.insert(nb, tableau2[y])
        else:
            x = 0
            while True:
                if tableau2[y] <= triTableau[x]:
                    x += 1

                else:
                    triTableau.insert(x, tableau2[y])
                    break

        nb += 1


        count += 1
        #print(nb)
        #print(tableau2[nb])
        #nb -= 1

    #del(triTableau[0])
    print(tableau1)
    print(tableau2)
    print(triTableau)
    print(count)


fonctionDeTri(tableau1)
print("------------------------------------------")
fonctionDeTriPlusieursTableaux(tableau1, tableau2)
