
"""
Cinema age management system
if someone is under 12 
        U, PG and 12 films available

if someone is under 15
        U, PG, 12 and 15 films available

if over 18
        All available
"""
age_input = int(input("How old are you please?"))
print(f"Thank you, you are {age_input} years old")
def which_films_are_suitable(user_age):
    if user_age <= 12:
        print("Thank you, you can watch all U, PG and 12 rated films")
        
    elif user_age <= 15:
        print("Thank you, you can watch all U, PG, 12 and 15 rated films")
    else:
        print("""Thank you, you can watch all films!!
              U, PG, 12, 15 and 18 rated films""")
        
which_films_are_suitable(age_input)
 
 
"""
 Chatbot greetings
 
 btwn 05:00 - 12:00  Good Morning
 btwn 12:00 - 18:00   Good Afternoon
 btwn 18:00 - 12:00 Good Evening
 """  

# 24hr clock 
time = 26
 

if time > 5 and time < 12:
    print("Good Morning")
elif time > 12 and time < 18:
    print("Good Afternoon")
elif  time > 18 and time < 24:
    print("Good Evening")
else:
    print("Please check your timezone!")