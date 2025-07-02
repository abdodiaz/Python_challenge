import math
# def factoriale (n):
#    return math.factorial(n)

# print(factoriale(5))    


# def multi(m) :
#             count = 1
#             result = 0
#             while count <= 10 :
#                result = m * count
#                count+=1
#                print(result)
            
# print(multi(2))    
     

L = int(input(" Entrez un nombre : "))

est_carre_parfait = False
i = 0

while i * i <= L:
        if i * i == L:
            est_carre_parfait = True
            break
        i += 1

if est_carre_parfait:
   print(f"{L} est un carré parfait.")
else:
    print(f"{L} n’est pas un carré parfait.")
    
