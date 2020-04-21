# Deleting Duplicates in a list

List = [1,2,3,4,4,6,7,8,9,9,10]
unique =[]

for number in List:
    if number not in unique:
        unique.append(number)
print(unique)  