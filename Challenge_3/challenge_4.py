def rechercheElement(element, liste):
    i = 0
    while i < len(liste):
        if liste[i] == element:
            return i  
        i = i + 1
    return False  

liste = [10 , 3, 7, 8, 6]
print(rechercheElement(3, liste))  
print(rechercheElement(9, liste))  
