
notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]

moyenne = sum(notes) / len(notes)

notes_superieures = []

for note in notes:
    if note > moyenne:
        notes_superieures.append(note)

print("Moyenne des notes :", moyenne)
print("Notes supérieures à la moyenne :", notes_superieures)
