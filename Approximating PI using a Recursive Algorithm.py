# approximating PI using a recursive algorithm:
import math

pi = 3.14159265#35897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

#this will currently approximate PI to "8" decimal places! .......which by the way is the farthest this code goes before crashing!!!

PI = [3,1,4,1,5,9,2,6,5]  #putting the digits in a list so I can reference how many decimals there are in my final statement.


#below will print out the Recursive value then the approximation for each iteration:


approx = 1
y = 3
x = 1
n = 1
print(n)
i = 0
while y != pi:
    
        approx = (3*(2**i))*x
        y = round(approx,8)   # "8" because that is the amount of decimal places we want our accuracy to be at.
        print(y)
        
        print()
        
        if y == pi:    #added these two lines so the next "n" wouldn't print once I have found the approximation I was looking for.
           break
        
        n = math.sqrt(2.0 - math.sqrt(4.0-(n**2.0)))
        x = round(n,16)
        print(x)
        i = i + 1



L = len(PI)-1  #the length of my list of digits in my approximation at the start of the program...........Had to subtract 1 since I just want the decimal place (everything but the 3).

print("Your APPROXIMATION to 8 digits: " + str(approx))     
print("Your APPROXIMATION to PI is " + str(L) + " decimal places: " + str(y))
print ("It took " + str(i) + " iterations to achieve this approximation")

