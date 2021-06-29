#a BREAK is used to terminate the loop entirely.
#a CONTINUE skips to the next iteration of the loop.
#a PASS does nothing and acts as a placeholder

#break:
while True:
    name = input("Enter your name: ")
    if name != "":
        break #breaks us out of the loop

#continue:
phone_number = "123-456-7890 "

for i in phone_number: #goes through each iteration of the phone number string
    if i == "-": #if the loop is at a dash (-)
        continue #skips to the next iteration of the loop
    print(i, end = "") #prints each phone number iteration, ending with "" so we don't print it seperately on each line.

print("\n") #makes a new line so its cleaner for the next thing: pass.

#pass:
for j in range(1, 21): #lets say i don't want to print 13 when printing all of these.
    if j == 13:
        pass
    else:
        print(j, end = ", ")    