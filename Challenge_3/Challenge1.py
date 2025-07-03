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

print("Moyenne : ", moyenne)
print("Notes supérieures à la moyenne : ", notes_sup)




