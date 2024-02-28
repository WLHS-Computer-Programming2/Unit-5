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