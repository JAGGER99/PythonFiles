# Function Demo

def greet_user():
# these 2 print statements will only be excuted if the function is called!!!                   
    print('hi there!')
    print('Welcome aboard')

 
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
greet_user("John") # here we reference the function and any where the parameter "name" is we replace with "John"
print("Finish")
    




















