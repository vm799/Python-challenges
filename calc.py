"""
Build a calculator
"""

def add(num1, num2):
    return num1+ num2

def minus(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return round((num1 / num2),2)


num1 = int(input("Type in first number:  "))
num2 = int(input("Type in second number:  "))
        
calculation = input("""
        Type 1  to add, 
        Type 2  to minus,  
        Type 3  to multipy,
        Type 4  to divide these numbers
        type 'end' to finish
        
        :_ """)

if calculation == "1":
            print(num1, "+", num2, "=", add(num1, num2))
elif calculation == "2":
            print(num1, "-", num2, "=", minus(num1, num2))

elif calculation == "3":
           print(num1, "x", num2, "=", multiply(num1, num2))
elif calculation == "4":
           print(num1, "/", num2, "=", divide(num1, num2))
elif calculation == "end":
   print("okay bye!")
        
