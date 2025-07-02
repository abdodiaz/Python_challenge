import math

x1 = float(input("Entrez x1 : "))
y1 = float(input("Entrez y1 : "))
x2 = float(input("Entrez x2 : "))
y2 = float(input("Entrez y2 : "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Distance entre les deux points :", distance)
