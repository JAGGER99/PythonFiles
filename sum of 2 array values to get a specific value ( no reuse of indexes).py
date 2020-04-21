# Finding the sets of numbers from an array that when summed get you a particular value

array = [2,3,6,7,11,15]  #array given
target = 9               #value we want to be summed up to
New_array = []
x=0
y=0

for i in range(len(array)):
    for j in range(len(array)):
        if array[i] + array[j] == target:
            x = array[i] 
            y = array[j]
            
            if (y,x) not in New_array:    # this only gives us values that haven't been used yet!
                New_array.append((x,y))
                
print(New_array)