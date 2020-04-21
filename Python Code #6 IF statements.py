# IF Statement DEMO:

is_Hot = False
is_Cold = True


if is_Hot:
    
    print("it is a hot day today") # this will not show because the condition is False!
    
elif is_Cold:

    print("it is a cold day today") #this will run since is_Cold is True!
    
else:
    print("Have a nice day") # wont see this because one of the above is True!


############################
#############################
############################
    
#logical operators:
    
has_high_income = True
has_good_credit = True
criminal_record = False
    
if has_good_credit and has_good_credit and not criminal_record: #the "not" says that if criminal_record is False then excute the command.
    print("Elligible for loan")


if has_good_credit or criminal_record: #only one of the conditions has to be true to execute the command.
    print("Possibly elligible for loan")
    
###############################
#############################
###########################
    
#Comparison Operators : 
    
temperature = input("What is the temperature outside? ")


if int(temperature) > 30:
    print("it is a hot day")
    
elif int(temperature) < 10:
    print("it is a cold day")
    
else:
    print("it is a nice day")
    

################################
    
name = input("What is your username? ")

if len(name) < 3:
    print("Your username must be at least 3 characters long!")
    
elif len(name) > 50:
    print("Your username cannot be longer than 50 characters!")
    
else:
    print("Great!")
    
##################################
    






