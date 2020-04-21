# Function Demo

def greet_user():
# these 2 print statements will only be excuted if the function is called!!!                   
    print('hi there!')
    print("Welcome Aboard")

 
print("Start")
greet_user() # here we reference the function (after it has been defined ofcourse!)
print("Finish")
    



########################
########################
########################
##########################
print()
#Passing information to our functions using parameters:

def greet_user(name):
# these 2 print statements will only be excuted if the function is called!!!                   
    print(f'Hi {name}!')
    print('Welcome aboard')

 
print("Start")
greet_user("John") # here we reference the function and any where the parameter "name" is we replace with the argument "John"
print("Finish")
    
#############################
############################
#############################
#############################
print()


# when you have two parameters:
def greet_user(first_name, last_name):
# these 2 print statements will only be excuted if the function is called!!!                   
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')

 
print("Start")
greet_user("John", "Tron") # here we reference the function and any where the parameters " first_name"  and "last_name" are replaced with the positional arguments "John" and "Tron"
print("Finish")

###########################
##############################
##############################
#############################

def greet_user(first_name, last_name):
# these 2 print statements will only be excuted if the function is called!!!                   
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')

 
print("Start")
greet_user(last_name = "John", first_name = "Tron") # here we reference the function and any where the parameters " first_name"  and "last_name" are replaced with the key word arguments "John" and "Tron"
print("Finish")

#NOTE: key word arguments are normally used when trying to improve the readability of your code

#positional arguments MUST come before key word arguments. otherwise you will get an error

 