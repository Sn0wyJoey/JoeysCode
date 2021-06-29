#The variable scope is the place a variable is recognized. A variable is only available from the region it is created.
#A global and locally scoped version of a variable can be created. 

name = "GlobalScope" # global scope. This variable is available inside and outside functions.

def display_name():
    name = "LocalScope" #local scope. This variable is only available inside this function.
    print(name)

display_name() #prints LocalScope, the local scope
print(name) #prints GlobalScope, the global scope