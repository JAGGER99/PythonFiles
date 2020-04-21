# 2D lists Demo

matrix = [
        
[1,2,3], [4,5,6], [7,8,9]          # 3 ROWS and 3 COLUMNS
        
]

print(matrix[0][1]) # prints the element in the first row and second column!

print(matrix)
print()

###################
for row in matrix:

    for column in row:
        print(column)

####################    
  
for row in matrix:
    print(row)
######################
print()


for row in matrix:   #for each element in the list called "matrix" ...
    
    print()