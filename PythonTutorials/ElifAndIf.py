age = int(input("How old are you?: ")) 

if age == 100: #use double equal signs to check if one is equal to another. It is the comparison operator for equality. If you use one equal sign, thats the assignment operator for equality.
    print("You are 100 years old")
elif age >= 18 :
    print("You are an adult") #make sure to indent right
elif age < 0:
    print("You haven't been born") #checks another statement. Elif is between if and the last else.
else:
    print("You are a child")