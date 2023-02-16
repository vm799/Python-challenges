

"""
Take in the scrabble word as a string
split each letter into an individual string
iterate over the ist of string letters
assign the correct scores for each
print the total score at end
"""

one_point_letter =["a", "b", "c", "d", "e", "f"]
two_point_letter =["g", "h", "i", "j", "k", "l"]
three_point_letter =["m", "n", "o", "p", "q", "r"]
four_point_letter =["s", "t", "u", "v", "w", "x","y", "z"]

def scrabble_calc():
    word_score=0
    
    word = input("Please type in your scrabble word to return your score:  ")
    
    letter_list = [x for x in word]
    print(letter_list)
    for letter in letter_list:
        if letter in one_point_letter:
            word_score += 1
        elif letter in two_point_letter:
            word_score += 2
        elif letter in three_point_letter:
            word_score += 3
        elif letter in four_point_letter:
            word_score += 4
    print(f"Your word score is:   {word_score}")   
scrabble_calc()  