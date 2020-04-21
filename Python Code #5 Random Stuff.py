print(" ")

course = 'python for "beginners"'
print(course)
######################
print(" ")

print(course[1])
######################
print(" ")

print(course[-1])
#####################
print(" ")

print(course[0:3])
######################
print(" ")

print(course[:])
####################
x = course[:]
print(x) 
####################
print(course[0:-1]) #starts at p and ends at s excluding the " on the end (it does not include the character in the -1 spot)

###########################################################
############################################################
#############################################################
###############################################################

first_name = 'John'
last_name =  'Smith'

message1 =  first_name + ' [' + last_name + '] ' + 'is a coder!'

print(message1)

#formatted String Demo:

first_name = 'John'
last_name = 'Smith'

message2 = f'{first_name} [{last_name}] is a coder!'
print(message2)

####################################################################
#STRING METHODS DEMO:

course = 'python for beginners'
len(course)   #tells us how may characters are in the string.
print(len(course))

######################
print(course.upper()) #makes all capital 
print(course.lower()) #makes all lower case

print(course.find('p')) # prints the first place a p is found.

print(course.replace('beginners', 'absolute beginners')) 

print('python' in course) #sends back boolean value (true)
print('Python' in course) #sends back a boolean value (false because case sensitive)


#########################
########################
#######################
########################

#arithmatic operations

print(10 + 3)
print (10 - 3)
print(10/2)
print(10/3)
print(10//3) #rounds to an integer
print(10 % 3) #returns the remainder of 10/3 (which returns 1).


x = 10
x = x + 3 # x += 3  ... known as the "augmented assignment operator".
print(x)

#######################

#operator precedence:

#without parentheses
#1 exponents
#2 multiplication/division
#3 addition/subtraction

x = (3+719)*12 - 5*2

print(x)
##########################

#other mathematical operators


x = 2.7
round(x) #rounding to the next integer
print(round(x))
###########################
x= -2.5
abs(x) #absolute value of x
print(abs(x))


import math #imports the math library

x= 2.3

math.ceil(x) # turns into the next highest whole number

print(math.ceil(x))

math.floor(x) # turns into the next lowest whole number

print(math.floor(x))





