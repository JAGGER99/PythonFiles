# Creating random variables Demo:

import random


for i in range(3):
    x = random.random() # a random value from 0 to 1
    print(x)

for i in range(3):
    y = random.randint(10,20) # specify the range of calculating a random integer
    
 #####################################################
    
members = ['bob', 'john','jill']

leader = random.choice(members)
print(leader)


######################################################

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first , second     # "return" automatically puts the integers in point notation.... ex. (x,y)
        
    
dice1 = Dice()
dice1.roll()
print(dice1.roll())

 



 