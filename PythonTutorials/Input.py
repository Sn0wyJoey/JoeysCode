name = input("What is your name?: ") #asks user for name and stores it in the name variable
age = int(input("How old are you?: ")) #asks for the age and stores it in an integer variable
height = float(input("How tall are you(in cm)?: ")) #asks for the height and stores it in a float variable

age = age + 1

print("Hello " + name)
print("You are " + str(age) + " years old.")
print("You are " + str(height) + "cm tall")