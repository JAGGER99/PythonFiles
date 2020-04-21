# ordering a list of (x,y) points according to ascending y values:

# the points (4,3),(5,2),(3,7)
array1 = [4,5,3] #x values
array2 = [3,2,7] #y values

#printing points

for j in range(len(array1)):
    print("(" + str(array1[j]) + "," + str(array2[j])+")")

print()
#while loop for switching points

while True :
    k = 0
    for i in range(len(array1)-1):    # runs three times ; the range = 0 1 2     ...   # range starts at 0
       
        if(array2[i] > array2[i+1]):
            
            
            # moving the x values:    
            x = array1[i]                  #
            array1[i] = array1[i+1]        #  switches the spots of the x's 
            array1[i+1] = x                # 
            
            
            # moving the y values:    
            y = array2[i]                  #
            array2[i] = array2[i+1]        #  switches the spots of the y's
            array2[i+1] = y                #
            
            # counters
            i = i + 1
            k = k + 1
            
    if k == 0:
        break
        
for j in range(len(array1)):
    print("(" + str(array1[j]) + "," + str(array2[j])+")")


