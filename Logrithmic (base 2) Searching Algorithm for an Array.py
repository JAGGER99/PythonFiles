
#effeciently searches through an Array using Big O [Log(base 2)n  =10 (in this case)]  ....essentially the number of times the loop runs:

myArray = [1,5,3,4,2,6,9,10,7,8]
        #  0 1 2 3 4 5 6 7  8 9
myNum = 5

myArray.sort()
print(myArray)
print()

x = len(myArray)   #10


while myNum != myArray[x-1] and len(myArray)!= 1:   
    
    x = len(myArray)//2   #cutting the array in half
    
    
    for i in range(0, x): 
        myArray[i] = int(myArray[i]) # casting the elements in myArray as integers so I can compare their values below in the IF statements
    
    
    if myNum < myArray[x-1]:
        myArray = myArray[0:x]
      
    elif myNum > myArray[x-1]:
        myArray = myArray[x:]
        
        
if len(myArray) == 1:
    print("My Num not found")
    
if myNum == myArray[x-1]:
    print("My number is " + str(myArray[x-1]))
    