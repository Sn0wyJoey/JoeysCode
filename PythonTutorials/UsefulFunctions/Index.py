#the index operator gives access to a sequence's element (like a str, list or tuple)

name = "joey Brar!"

if(name[0].islower()): #checks if the first letter in name is lower case
    name = name.capitalize() #capitalizes the first letter in name

print(name)

first_name = name[:4].upper()  #creates a substring with "joey" and makes it all upper case 
last_name = name[5:].lower() #creates a substring with "Brar" and makes it all lower case
last_character = name[-1] #creates a substring of the last character

print(first_name)
print(last_name)
print(last_character)