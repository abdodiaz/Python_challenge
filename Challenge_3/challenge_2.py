Ch1 = "Le langage Python est très populaire"
Ch2 = "Python est un langage puissant"

mots1 = Ch1.split()
mots2 = Ch2.split()

mots_communs = []
for mot in mots1:
    if mot in mots2 and mot not in mots_communs:
        mots_communs.append(mot)

print(" Mots communs : ", mots_communs)