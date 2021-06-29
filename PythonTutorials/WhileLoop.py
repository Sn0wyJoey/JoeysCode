#A while loop is a statement that will execute it's code as long as it's condition is true.

name = input("What is your name? (don't leave this blank!) ")

while len(name) == 0: #If the name does not have any characters, or in other words the user didn't type their name, then we keep asking for it.
    name = input("Enter your name, I will keep asking. ") 

print("Hello, " + name, end = "!")