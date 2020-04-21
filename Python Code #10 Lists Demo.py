# Lists Demo
names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
names[0] = "Bob"
print(names[0]) #first item in list
print(names[-1]) #last item in list
print(names[-2])
print(names[-3])
print(names[2:4]) #get all itmes from 3rd to 4th item
print(names[:]) #returns all in list


###########################################
###########################################
##########################################

# calculates the highest number in the list
numbers =  [3,6,2,8,4,10]
max = numbers[0] #set as default

for number in numbers:
    
    if number > max:
        max = number
print(max)

############################################
############################################
############################################
print()

#replacing a certain character from a String:
name = "Joshua Greene"
new_name = name.replace(" ","*")   #replaces spaces with "*"
print(new_name)