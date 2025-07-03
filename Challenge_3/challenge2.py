Ch1 = "langage Python est populaire "
Ch2 = "Python est un langage de programation"

mots1 = Ch1.split()
mots2 = Ch2.split()

communs = []
for mot in mots1:
    if mot in mots2 and mot not in communs:
        communs.append(mot)

print(" Mots communs : ", communs)