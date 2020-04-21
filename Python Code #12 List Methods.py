# List Methods
numbers = [5,2,1,7,4]
numbers.append(20) # adds element at end of list
numbers.insert(0,10) # first number represents the placement in the list and the second number is the actual number you want to insert.
numbers.remove(2) # removes the 2 in the list
numbers.index(5) # looks for the placement of 5 in the list

print(numbers.index(5))


numbers.clear() # empties list
numbers = [2,5,3,7,43]
numbers.pop() # removes the last element in your list

print(numbers)

numbers.sort() # sorts the values in your list from least -----> greatest value
numbers.reverse() # sorts the values in your list from greatest -----> least value
numbers2 = numbers.copy() #copies your list and puts it in the variable numbers2
 

print(numbers2)

print(50 in numbers) # will check if 50 is in your list. Will return True or False


print(numbers)

