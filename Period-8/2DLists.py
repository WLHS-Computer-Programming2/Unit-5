'''
Name: Mr. Smith
Date: 2/26/24
Lesson: Unit 5
Topic: 2D Lists
'''

# 2D lists are like a grid
#           0  1 2  3 4 5 6 7
my_grid = [[-3,2,0,-1,7,8,3,9], # row 0
            [5,9,-3,-5,3,9,0,-9], # row 1
            [2,0,3,3,7,8,3,2],
            [9,-3,7,7,3,9,0,9],
            [3,3,7,8,3,2,7,8],
            [7,3,3,3,7,8,3,9],
            [2,7,7,3,3,-5,7,8],
            [9,-3,7,7,7,-5,3,9]
]

# print the first row
print(my_grid[0])

#print the last row
print(my_grid[7])
print(my_grid[-1])
print(my_grid[len(my_grid)-1]) 
# len(my_grid) returns the number of rows

# print [7,7,7] from the last row
# Steps: access last row, access slice of 7,7,7
print(my_grid[-1][2:5])

# print 2nd through 5th rows
print(my_grid[1:5])
for i in range(1,5):
    print(my_grid[i])

# print all of the data from the 3rd column
# should print [0,-3,3,7,7,3,7,7]
    




