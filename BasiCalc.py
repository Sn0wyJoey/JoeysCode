import colors  as c
from math import *

welcome = (c.random_color() + """ __________
| ________ |
||12345678||
|\"\"\"\"\"\"\"\"\"\"|
|[M|#|C][-]|
|[7|8|9][+]|
|[4|5|6][x]|
|[1|2|3][%]|
|[.|O|:][=]|
\"----------\" """)
welcome2 = (c.random_color() + "Welcome to the Calculator!")
print(welcome)
print(welcome2)

while True:
    op = input(c.random_color() + "To enter your operator, type the\nnumber that matches the order of\n(+,-,x,/,x^y,√). For an example:\nType a 1 for addition, type a 2\nfor subtraction, 6 to do square\nroot, etc. Type Here: > ")
    num1 = float(input(c.random_color() + "Great Job! Now type in\nthe first number for your calculation > "))
    num2 = float(input(c.random_color() + "Now type the 2nd number\n(If you chose option 6 last time then type 0) > "))

    if op == "1":
        print(num1 + num2)
    elif op == "2":
        print(num1 - num2)
    elif op == "3":
        print(num1 * num2)
    elif op == "4":
        try:
            print(num1 / num2)
        except ZeroDivisionError as e:
            print(c.red + "ERROR: " + str(e))
            print("You can't divide by zero!")
    elif op == "5":
        print(num1**num2)
    elif op == "6":
        print(sqrt(num1))
    else:
        print(c.red + "Error: Invalid Operator; You\nneed to type in 1, 2, 3, 4, 5, or 6\n for the operator, and a number for the calculation.")
        break
    again = input(c.yellow + "Do you want to go again? Type 1 for yes, and anything else for no. > ")
    if again == "1":
        pass
    else:
        break

print(c.magenta + "Thank you for using Calculator, come back soon!")
exit()