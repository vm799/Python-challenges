#____________________Challenge 3_____________________#

"""
Write a sort function of the items in a list. WITHOUT the sort function
"""

my_list = [2, 33 ,3, 345, 8, 1]
sorted_list =[]

while my_list:
    minimum = my_list[0]
    for x in my_list:
        if x < minimum:
            minimum = x
    sorted_list.append(minimum)
    my_list.remove(minimum)
    
print(sorted_list)

my_list = [2, 33 ,3, 345, 8, 1]
sorted_list =[]

while my_list:
    maximum = my_list[0]
    for x in my_list:
        if x > maximum:
            maximum = x
    sorted_list.append(maximum)
    my_list.remove(maximum)

print(sorted_list)


