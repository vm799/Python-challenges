import random

#____________________Challenge 9_____________________#

"""
Write a Python program to search an array for an item
"""
num_list=[]

for i in range(0,20):
    num_list.append(random.randint(1,20))
print(num_list)

elem_to_find = 10
x = num_list.find(elem_to_find)
print(x)
