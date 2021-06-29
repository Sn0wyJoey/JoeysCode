# args is a perameter that will put all arguments into a tuple. It is useful so that a function can accept
# a varying amount of arguments.  []

#Example:

def add(num1, num2):  #is as function that takes in 2 numbers and returns the sum
    sum = num1 + num2
    return sum

# print(add(1, 2, 3)) 
#       ^ This would print an error, because we are giving it 3 arguments instead of 2.

# Here is the solution:

def add1(*args): #make sure you have the asterisk. It doesn't have to be args, it can be named anything.
    sum = 0
    args = list(args) #changes the tuple to a list so we can change it.
    for i in args:
        sum += i 
    return sum

print(add1(1, 2, 3, 4, 54, 1)) #we can add any amount of arguments we want.