#____________________Challenge 10_____________________#

"""
Write a Python program to implement a binary search
"""


def binary_search(list, target):
    #O(n)
    first = 0
    last = len(list)-1
    
    #while loop increases time complexity
    while first <= last:
        mid = first + last // 2
        if list[mid]==target:
            return mid
        
        elif list[mid] < target:
            first = mid +1
            
        else :
            last  = mid - 1
    else:
        return None
        
    
def verify(index):
    if index == None:
        print ("Target not found")
    else:
        print(index)
        
result = binary_search([1,2,3,4,5,6,7,8], 8)
verify(result)
    