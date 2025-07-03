chaine = input("Entrez une chaîne : ")

i = len(chaine) - 1

inverse = ""

while i >= 0:
    inverse += chaine[i]
    i -= 1

print("Chaîne inversée :", inverse)
