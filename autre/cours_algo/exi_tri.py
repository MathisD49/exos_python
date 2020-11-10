#1

tableau = [2, 5, 6, 4, 1, 8, 9, 3, 7]
permute = True

while permute:
    permute = False
    for i in range(len(tableau)-1):
        if tableau[i] > tableau[i+1]:
            a = tableau[i+1]
            tableau[i+1] = tableau[i]
            tableau[i] = a
            permute = True



print(tableau)
