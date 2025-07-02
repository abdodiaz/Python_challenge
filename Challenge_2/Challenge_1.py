def horaire_sup (nom, salaire_horaire,nomber_heurs):
    
    while True :
        try:
            if nomber_heurs > 40 :
              hd =(nomber_heurs-40)
              net = (hd * 1.5) + salaire_horaire*40 
              return net 
            else:
                net = salaire_horaire *nomber_heurs
                return net
        except ValueError as e:
            return e

print(horaire_sup("ahmed",10,50))
    