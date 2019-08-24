#The function should return the total number of unique letters in the string.

letters= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
    uniques=0
    for letter in letters:
        if letter == word:
            uniques+=1
    return uniques
            
    
print(unique_english_letters("mississippi"))
