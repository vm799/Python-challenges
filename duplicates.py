import random

#____________________Challenge 7_____________________#

"""
Write a Python program to check for duplicates
"""

word_list= ["boo", "job", "boo", "job", "boo", "job"]

num_list =[]
num = 10 
for i in range(num):
    num_list.append(random.randint(0, num))
print(num_list)

print(set([x for x in word_list if word_list.count(x)>1]))

print(set([x for x in num_list if num_list.count(x)>1]))
