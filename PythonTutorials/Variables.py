variableName = 'Hello'
Name = "Joey" #string data type
age = 13 #when assigning an integer variable, don't put quotation marks or it would be a string.
gpa = 3.5 #float data type (has a decimal)

print(variableName + ", " + Name + "! You are " + str(age) + " years old and")
print("have a gpa of " + str(gpa) + ".")
#when we want to put a non string in a string, we put str(integerVariable) to
#make it into a string, because we cant combine a non-string with a string

subscriptions = 5
subscriptions = subscriptions + 1
print(subscriptions)
print(type(subscriptions)) #prints the data type of the variable
print(type(Name)) 

isSmart = False #boolean data type
isTall = True
print(isSmart)
print(isTall)
print(type(isSmart)) #prints the type of variable, so boolean.

print("Are you smart? " + str(isSmart)) #do the str(variable) because a boolean is not a string
#and we want to put it in the string.

#The 4 basic types of data types to store in variables are:

#string, a series of characters

#int, which store a whole number (an integer)

#float, which are floating point values (a number with a decimal)

#boolean, a true or false value