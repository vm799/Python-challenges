
#____________________Challenge 1_____________________#

"""
Write a Python program to fiND all the prime numbers between 100 and 200.
"""

for num in range(100,200):
    if all(num%i !=0 for i in range(2, num)):
        print(num)
