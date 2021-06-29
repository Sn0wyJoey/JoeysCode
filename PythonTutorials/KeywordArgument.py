#Keyword Arguments are arguments preceded by an identifier when we pass them to a function.
#The order of the arguments doesn't matter, unlike the positional arguments that do matter.
#Python knows the names of the arguments that our function receives.

#Example of a positional argument:
print("Examples of a positional argument:\n")

def hello(first, middle, last):
    print("Hello, " + first + " " + middle + " " + last)

hello("Joey", "Singh", "Brar") #the order of these arguments matter. If we switched it around:
hello("Singh", "Brar", "Joey") #it would return something else.

#If we used keyword arguments, the order of these arguments doesn't matter, but with each argument
#we need to precede each argument with a unique identifier. That identifier is the name of the perameter
#we want to associate each argument with. so:

hello(middle = "Singh", last = "Brar", first = "Joey") #the order we put it in doesn't matter because we set it equal to middle, last and first.