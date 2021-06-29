 #a function is a block of code which is executed only when it is called
def hello(name): #defines a function that does what is in it.
    print("Hello, " + name)
    print("Have a nice day!")

hello("Joey") #calls the function hello
       #^ When you send information to a function, that is called arguments. It is the information we are sending to a function.
       #When we define that function, we need a matching set of perameters.

name = "Dude"
hello(name)

print("\n\n")

def full_name(first_name, last_name, age):
    age = age + 10
    print("Hello, " + first_name + " " + last_name + "!")
    print("You will be " + str(age) + " years old in 10 years!")

age = int(input("Enter your age(In numbers): "))
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name(first_name, last_name, age)