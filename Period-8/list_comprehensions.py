'''
Name: Mr. Smith
Date: 2/28/24
Lesson: List Comprehensions

'''

# filling up a list with 1-5
nums = []
for i in range(1,6):
    nums.append(i)
print(nums)

# new way - list comprehensions
nums = [i for i in range(1,6)]
print(nums)

# use list comprehension to make the
# list [2,4,6,8,10] in two different
# ways

nums = [i*2 for i in range(1,6)]
print(nums)

nums = [i for i in range(2,12,2)]
print(nums)

# make the list [0,1,0,1,0,1]
# hint: remainders

zero_one = [i%2 for i in range(0,6)]
print(zero_one)

import math
zero_one = [round(abs(math.sin(i*math.pi/2))) for i in range(0,6)]
print(zero_one)
# make the list [True,False,True,False,True,False]
zero_one = [i%2==0 for i in range(0,6)]
print(zero_one)

zero_one = [bool(i%2) for i in range(1,7)]
print(zero_one)

string_nums  = [str(i) for i in range(1,6)]
print(string_nums)

# make the list [1,4,7,10,13]
#[0,1,2,3, 4]
#[1,4,7,10,13]
# linear, rate of change is 3
nums = [3*i+1 for i in range(5)]
print(nums)

# challenge: make the list [0,7,16,27,40,55]
# hint: not linear, is in the form x^2 + b*x
nums = [n**2+6*n for n in range(6)]
print(nums)

# extra content - boolean expressions inside
# of list comprehensions
# format: [<expression> for item in list if <condition>]
# same as
'''
for item in list:
    if conditional:
        expression
'''
list_one = [22,13,45,50,98,71,44,1]
evens = [x for x in list_one if x%2 == 0]
fun_list = [x if x%2==0 else 2*x for x in list_one]
print(fun_list)