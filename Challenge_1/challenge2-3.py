nom = input("votre nom : ")
while True :
    try:
        salaire_horaire = float(input("votre salaire : "))
        nomber_heurs = float(input("votre heur de travaille : "))
        if nomber_heurs > 40 :
          hd =(nomber_heurs-40)
          net = (hd * 1.5) + salaire_horaire*40  
        else:
            net = salaire_horaire *nomber_heurs
        break
    except ValueError as e:
        print(e)
print(f" votre nom :{nom} , le salaire est : {net}")

