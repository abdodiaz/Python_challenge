while True :
    try : 
        n1 = float(input("n1 : "))
        n2 = float(input("n2 : "))
        produit= n1 * n2
        if produit == 0 :
            print("null")
        elif produit > 0 :
            print("pos")
        else  :   
            print("neg")
    except ValueError as e : 
        print(e)
 