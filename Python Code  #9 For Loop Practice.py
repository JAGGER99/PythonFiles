# For Loop Demo

for item in "Python":
    print(item)
    
print()
##########################

for item in ['jo', 'bob', 'mary']:
    print(item)

############################
print()

for item in range(10):
    print(item)
###########################
        
print()

for item in range(5,10,2):
    print(item)
##############################

prices = [10,20,30]

total = 0;
for price in prices:
        total = total + price
print(f"Total: {total}")
###############################
##############################

#nested loops demo

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

##############################
##############################

numbers = [5,2,5,2,2]

for num_X in numbers:
    print("X"*num_X)
    
    
print()
###############################
#Does the same thing as directly above:
    
numbers = [2,2,2,2,5]

for num_X in numbers:
    output = ''
    for count in range(num_X):
        output += "x"
    print(output)
 
    
    