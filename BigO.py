def linear_search(list, target):
    """Returns the index of the target
    or None if not found"""
    
    for i in  range(0, len(list)):
        if list[i]== target:
            return i
    return None

def verify(index):
    if index == None:
        print ("Target not found")
    else:
        print("Target found at index:", index)
        
result = linear_search([1,2,3,4,5,6,7,8,9], 7)

verify(result)    