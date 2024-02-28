'''
Name: Mr. Smith
Date: 2/28/24
Lesson: List Comprehensions

'''

# old way
nums = []
for i in range(1,6):
    nums.append(i)
print(nums)

# new way - list comprehensions
nums = [i for i in range(1,6)]
print(nums)

# use list comprehension to make the
# list [2,4,6,8,10] in two different
# way

even_nums = [i for i in range(2,12,2)]
print(even_nums)

even_nums = [i*2 for i in range(1,6)]
print(even_nums)

import math
# make the list [0,1,0,1,0,1] using list comprehension
# hint: remainders
zero_one = [i%2 for i in range(0,6)]
print(zero_one)

# mathmagic way of doing it
zero_one = [round(abs(math.sin(i*math.pi/2))) for i in range(0,6,1)]
print(zero_one)

# make the list [True,False,True,False,True,False]
true_false = [i%2==0 for i in range(0,6)]
print(true_false)

string_list = [str(i) for i in range(1,6)]
print(string_list)

# make the list [1,4,7,10,13]
print([3*i+1 for i in range(5)])

# challenge: make the list [0,7,16,27,40,55]
# hint: not linear, x^2+bx+c and the domain is [0,5]
print([i**2+6*i for i in range(0,6)])

# extra content - boolean expressions in comprehensions
# format: [expression for item in list if conditional]
# is the same as
'''
for item in list:
    if conditional:
        expression
'''
list_one = [22,13,45,50,98,71,43,44,1]
print([x*2 for x in list_one if x%2==0]) # if statement
print([x+1 if x>=45 else x+5 for x in list_one]) # if else statement

# Google more for if, elif, else
