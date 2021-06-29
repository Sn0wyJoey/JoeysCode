# kwargs is a perameter that will pack all arguments into a dictionary. It is useful so that a function
# can accept a varying amount of keyword arguments.

# Example:

def hello(first, last):
    print("Hello " + first + " " + last)

#hello(first = "Joey", middle = "Hi", last = "Brar") Would return a error since it only accepts first and last name perameters and we put in a middle name

# Solution:

def hello1(**kwargs): #make sure you have TWO asterisks.
    #print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello, ", end = " ") #end = " " makes it on the same line
    for key, value in kwargs.items(): #iterates once through each key value pair
        print(value, end = " ") #end = " " makes it on the same line

hello1(title = "Mr.", first = 'Joey', middle = 'Hi', last = 'Brar')

