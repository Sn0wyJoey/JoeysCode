name = "joey brar"

print(len(name)) #prints the amount of characters in name, so 9 (including the space)
print(name.find("br")) #Tells the index of where "br" starts. (Index starts at 0). It would return 5 since it starts at 5
print(name.capitalize()) #Capitalizes the first letter of the string, so it would return Joey brar
print(name.upper()) #Makes the string all upper case, so it would print JOEY BRAR
print(name.lower()) #Makes the string all lower case, so it would print joey brar
print(name.isdigit()) #checks if the string is a digit(number), returns true if the string is a digit or false if it is not. It returns false if the string has both digits and letters in it 
print(name.isalpha()) #checks if the string has only letters, no numbers or spaces. Returns true if it does, or false if it doesn't
print(name.count("b")) #counts how many characters are in the string, so it would see how many b's are in our string and return the amount of b's there is, which is 1. 
print(name.replace("b", "a")) #replaces the "b" in our string with an "a". It would return "joey arar"
print(name*3) #prints the name 3 times. It would return "joey brarjoey brarjoey brar"