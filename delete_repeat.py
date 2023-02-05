
#____________________Challenge 15_____________________#

"""
Write a Python program to check string for repeat characters and return
a string without them.
"""

list1= [2,3,4,5,6,5,4,5,67,5656,767,77,44,33]
list2= [23,34,45,5,6,5,4,5,678,5656,767,77,44,33]
list4 = list(set(list1+list2))
print(list4)

str5 = [str(x)for x in list4]
print(str5)
