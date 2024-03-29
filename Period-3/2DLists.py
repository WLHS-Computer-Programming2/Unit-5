'''
Name: Mr. Smith
Date: 2/26/24
Lesson: Unit 5
Topic: 2D Lists
'''

# 2D lists are like a grid
my_grid = [[-3,2,0,-1,7,8,3,9],
            [5,9,-3,-5,3,9,0,-9],
            [2,0,3,3,7,8,3,2],
            [9,-3,7,7,3,9,0,9],
            [3,3,7,8,3,2,7,8],
            [7,3,3,3,7,8,3,9],
            [2,7,7,3,3,-5,7,8],
            [9,-3,7,7,7,-5,3,9]
]
#print(my_grid[7][2:5]) # prints 7,7,7 from last row
#print(my_grid[-1][2:5]) # prints 7,7,7 from last row
#print(my_grid[1:3]) # prints rows 1 and 2

# print all of the data from the third column
# should print [0,-3,3,7,7,3,7,7]
target = [0,-3,3,7,7,3,7,7]
column_three = []

for i in range(len(my_grid)):
    column_three.append(my_grid[i][2])
assert column_three == target

# try to do this with enumeration
for index,item in enumerate(my_grid):
    print(my_grid[index][2])

my_grid.append([100,100,100,100])
for item in my_grid:
    print(item)