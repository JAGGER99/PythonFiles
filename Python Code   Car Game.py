# CAR GAME
x = True
while x:
    
    Input1 = input('Type "help" for options ')

    while Input1 == "help":

        print("""
              
start - to start the car
stop - to stop the car
fast - to accelerate car
slow - to decelerate car""")
        
        Input2 = input("Which command would you like to execute? ")
    
        if Input2 == "start":
            print("the car has been started")
            Input3 = input("would you like to continue? (Y)es or (N)o? ")
            if Input3 == "N":
                print("The program has been terminated successfully")
                x = False
                break
            
        elif Input2 == "stop":
            print("the car has shut down")
            Input3 = input("would you like to continue? (Y)es or (N)o? ")
            if Input3 == "N":
                print("The program has been terminated successfully")
                x = False
                break
            
        elif Input2 == "fast":
            print("The car is accelerating!")
            Input3 = input("would you like to continue? (Y)es or (N)o? ")
            if Input3 == "N":
                print("The program has been terminated successfully")
                x = False
                break
            
        elif Input2 == "slow":
            print("The car is decelerating!")
            Input3 = input("would you like to continue? (Y)es or (N)o? ")
            if Input3 == "N":
                print("The program has been terminated successfully")
                x = False
                break
    
    else:
        print("Invald input please try again!")
    
    