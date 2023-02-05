
def is_anagram(s1, s2):
    """assign both strings to a set each 
    and if equates return true
    """
    return set(s1) == set(s2)
   
    
print(is_anagram("yob", "boy"))