notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]

# Calcul de la moyenne
somme = 0
for note in notes:
    somme += note
moyenne = somme / len(notes)

# Extraire les notes supérieures à la moyenne
notes_sup = []
for note in notes:
    if note > moyenne:
        notes_sup.append(note)

print(« Moyenne : », moyenne)
print(« Notes supérieures à la moyenne : », notes_sup)




**********
Ch1 = « Le langage Python est très populaire »
Ch2 = « Python est un langage puissant »

# Séparer les mots
mots1 = Ch1.split()
mots2 = Ch2.split()

# Rechercher les mots communs
communs = []
for mot in mots1:
    if mot in mots2 and mot not in communs:
        communs.append(mot)

print(« Mots communs : », communs)
*******
stock = [« Stylo », 25, « Classeur », 100, « Crayon », 12, « Surligneur », 40, « Feutre », 5]

# Afficher la liste initiale
print(« Liste initiale : », stock)

# Séparer les éléments
articles = []
quantites = []

for item in stock:
    if type(item) == str:
        articles.append(item)
    else:
        quantites.append(item)

# Trier les listes
articles.sort()
quantites.sort(reverse=True)

# Afficher le résultat
print(« Articles triés : », articles)
print(« Quantités triées : », quantites)

*******
L = [7, 23, 5, 23, 7, 19, 23, 12, 29]
a = 23

# Compter les occurrences
compteur = 0
for elem in L:
    if elem == a:
        compteur += 1

print(f »Nombre d’occurrences de {a} : », compteur)
***********
L = [7, 23, 5, 23, 7, 19, 23, 12, 29]
a = 23

# Compter les occurrences
compteur = 0
for elem in L:
    if elem == a:
        compteur += 1

print(f »Nombre d’occurrences de {a} : », compteur)