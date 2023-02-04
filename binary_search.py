#____________________Challenge 10_____________________#

"""
Write a Python program to implement a binary search
"""

def binary_search(array, low, high, x):
    if low > high:
        return -1
    mid = (low + high) // 2
    if array[mid] == x:
        return mid
    elif array[mid] > x:
        return binary_search(array, mid + 1, high, x)
    else:
        return binary_search(array, low, mid - 1, x)

# def binary_search(list, target):
#     #O(n)
#     first = 0
#     last = len(list)-1
    
#     #while loop increases time complexity
#     while True:
#         mid = first+last // 2
        
#         if list[mid] == target:
#             return mid
#         elif list[mid] > target:
#             last = mid-1
#         elif list[mid] < target:
#             first = mid +1
#         else:
#             return None
    
# def verify(index):
#     if index == None:
#         print ("Target not found")
#     else:
#         print(f"Target found at index: {index} ")
        
# result = binary_search([1,2,3,4,5,6,7,8], 8)
# verify(result)
    