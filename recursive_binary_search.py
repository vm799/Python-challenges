"""
    1. if list is empty return False
    2. if midpoint is equal to half the list and
    2a. target is bigger than mid slice the list from midpoint upwards
    and run function again
    2b. if target is less than midpoint slice the list down from 0 to midpoint
    and run function again
    """
    
def recursive_binary_search(list, target):
    if len(list)==0:
        return False
    else:
        mid = len(list)//2
        
        if list[mid]== target:
            return True
        
        else:
            if list[mid] < target:
                return recursive_binary_search(list[mid+1:], target)
            else:
                return recursive_binary_search(list[:mid], target)

        
        
        
def verify(result):
    if result == True:
        print("Hurray!")
    else:
        print("Not found in list")
        
found  = recursive_binary_search([1,2,3,4,5,6,7,8], 8)
verify(found)

found  = recursive_binary_search([1,2,3,4,5,6,7], 12)
verify(found)
