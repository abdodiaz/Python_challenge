L = [7, 23, 5, 23, 7, 19, 23, 12, 29]
a = 7

count = 0
for element in L:
    if element == a:
        count += 1

print(f"Nombre d'occurrences de {a} : ", count)