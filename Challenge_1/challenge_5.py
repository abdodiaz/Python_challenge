while True:
    try:
        N = int(input("int number "))
        count = 0
        result = 0
        while count <= N :
            result +=count 
            count +=1
        print(f"{result}")    
        
    except ValueError as e :
        print("fff") 
