# Finding how many "Mirror Dates" there are a year!
month = [1,2,3,4,5,6,7,8,9,10,11,12]
arrayTotal = []


for i in range(len(month)):
    if month[i] < 10:
        arrayTotal.append(month[i])
        
        print("(" + str(i+1) + "," + str(i+1) + ")")    


print(".........")
###############################################################


for j in range(len(month)):
    if month[j] >= 10:
        month[j] = str(month[j])    # need to make a string so i can switch the first and second digits!
        
        x = month[j][1] + month[j][0]   #reversing the order of the digits
       
        arrayTotal.append(x)
        
        print("(" + str(j+1) + "," + str(x) + ")")       # must be j+1 because zero based!!!
        
###################################################################################        
        
print(".........")    
print(len(arrayTotal))




