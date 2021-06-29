#nested loop is a loop inside of another loop
#lets create a rectangle using a nested loop.

rows = int(input("How many rows do you want? ")) #because we want a number, put it as an integer type.
columns = int(input("How many columns do you want? "))
symbol = input("What symbol do you want? ")

for i in range(rows): 
    for j in range(columns):
        print(symbol, end = " ") #the end = "" makes it so it doesn't print a new line after every time.
    print("") #prints another row after we finish the column so we can go to the next column