
def find_duplicates(elements):
    duplicates, seen = set(), set()
    
    for element in elements:
        if element in seen:
            duplicates.add(element)
        else:
            seen.add(element)
    print(duplicates)

group= [3,4,5,3,4,5,3,23,3,5,4, 23, 65]
find_duplicates(group)