#____________________Challenge 6_____________________#

"""
Write a Python program to check if word palindromic
"""

from distutils.command.check import check


check_word = "moonoom"

def palindrome_checker(word):
    if word == word[::-1]:
        print("Hurray yes it's a palindromic word")
    else:
        print("Sorry not a palindromic word")
        
palindrome_checker(check_word)

def palindrome_checker(word):
    if word == "".join(reversed(word)):
        print("Hurray yes it's a palindromic word")
    else:
        print("Sorry not a palindromic word")

palindrome_checker(check_word)