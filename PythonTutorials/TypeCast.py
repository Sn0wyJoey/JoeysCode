#type casting is converting the data type of a value to another data type

#example: 

x = 1 #int
y = 2.0 #float
z = "3" #string

#if we wanted to do math with these numbers, we couldn't because they all are different types of variables(one is a int, float, and string)
#lets convert y and z to an int.

# y:
int(y) #converts y to an int. we can also do print(int(y)) to print it.
int(z) #converts z to an int. To do math, we can do print(int(z) + x) which returns 4 (3 + 1 = 4, since we print z + x)

#if we wanted to convert x into a float and y into a string:

float(x)
str(y)

print(x)
print(str(y)) #turns it from a float to a string.
print(z)

print(int(x) + int(y) + int(z)) #turns all of the numbers into an int so we can add them, and then it adds them. (returns the sum of x, y and z)