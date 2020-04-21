#guess that number!

import random


guess_limit = int(input("How many guesses do you want?: ")) 

guess = input("I am thinking of a number between 1 and 100. You have " + str(guess_limit) + " tries. " + "What is my number? ")

number = random.randint(1,101)

try:
    val = int(guess)
    
    guess_count = 0
    
    while guess_count < guess_limit - 1:
        
        guess_count = guess_count + 1

        if val > number:
           x = input("your guess is too high! Guess again!: ")
           val = int(x)
        
        elif val < number:
            x = input("your guess is too low! Guess again!: ")
            val = int(x)
        else:
            print("YOU GOT IT!")
            print("it took you " + str(guess_count) + " tries!")
            
            if guess_limit >= 10:
                print("you beat the game in easy mode!")
            
            elif guess_limit <=5:
                print("you beat the game in hard mode!")
                
            break
        
    
    if guess_count >= guess_limit - 1:
        print(" ")
        print("YOU ARE OUTOF TRIES!!!!")
     

except ValueError:
    print("That's not a valid input!")   













    