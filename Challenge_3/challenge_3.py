stock = ["Stylo", 25, "Classeur", 100, "Crayon", 12, "Surligneur", 40, "Feutre", 5]


print("Liste initiale : ", stock)

articles = []
quantites = []

for item in stock:
    if type(item) == str:
        articles.append(item)
    else:
        quantites.append(item)

articles.sort()
quantites.sort(reverse=True)

print(" Articles triés : ", articles)
print(" Quantités triées : ", quantites)