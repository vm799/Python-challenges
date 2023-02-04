
#____________________Challenge 4_____________________#

"""
Write a Python program to print out all fibonacci numbers.
"""

def F(n):
    if n==0: return 0
    elif n==1: return 1
    else: return F(n-1)+ F(n-2)
    
for i in range(0, 20):
    print(F(i))
    


