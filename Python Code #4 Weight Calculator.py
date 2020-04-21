#6/26/19
#Joshua Greene

#weight calculator

weight_input = input("What is your weight?: ")

try:
   val = float(weight_input)
   
   weight_type = input("Is your weight in (L)bs or (K)g?: ")


   if weight_type == "K" or weight_type == "k":
    
    weight = float(weight_input)* (1.0/0.45)
    print("Your weight in pounds is: " + str(weight) + " kg")
    
   elif weight_type == "L" or weight_type == "l":
    
    weight = float(weight_input)* (0.45)
    print("Your weight in kilograms is: " + str(weight) + " lbs")
    
   else:
    print("Invalid Entry!")
   
   
except ValueError:
    print("That's not a valid input!")       


 
    
    