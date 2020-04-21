# unpacking demo

coordinates = (1,2,3)

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
######################
x,y,z = coordinates # this does the same thing as above!

###########################
###########################
###########################
###########################
#Dictionary Demo:
# ************************you cant assign the same key word to 2 differnt things!********************
customer = {} #empty dictionary
customer = {
        
        "name": "John Smith",
        "age": 30,
        "is_verified": True  
}
print(customer["name"]) #accesses the info stored in "name"
print(customer.get("age")) # does same thing but without giving you an error. If nothing assigned to that word then "None" will be returned

########################
########################
######################
#convert phone number to actual words:

phone_number = input("Phone #:")

numbers = {
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "0": "Zero"
} 
output = "" # creates a string that we add to every iteration of the for loop
for character in phone_number:
    output += numbers.get(character, "!") + " "   #if the dictionary does not have the number then displays "!"
    
print(output) 

print("")
########################
#########################
########################

nums = ["One","Nine","Seven","Five","Three","Two"]

number_conversions = {
     "One"  :   "1",
     "Two"  :   "2",
     "Three":   "3",
     "Four" :   "4",
     "Five" :   "5",
     "Six"  :   "6",
     "Seven":   "7",
     "Eight":   "8",
     "Nine" :   "9",
     "Zero" :   "0"
} 
 

output1 = "" # creates a string that we add to every iteration of the for loop
for word in nums[0:5]:
    output1 += number_conversions.get(word, "!")+ "-"   #if the dictionary does not have the number then displays "!"
    
output2 = number_conversions.get(nums[-1], "!")
    
print(output1 + output2)




