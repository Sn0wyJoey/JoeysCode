import colors as c
import sys

def Add(Num1 , Num2):
    return Num1 + Num2
def Multiply(Num1 , Num2):
    return Num1 * Num2
def Divide(Num1 , Num2):
    result = Num1 / Num2
    return round(result, 1)
def Subtract(Num1 , Num2):
    return Num1 - Num2
def print_answer(res):


    print("The answer is " , res)
Errors = ["usage: calc.py add/multiply/divide/subtract num1 num2" , "dude you didnt add any numbers!" , "Error: Add another number"]
Arguments = sys.argv
#test for errors 
if len(sys.argv) == 1:
    print(Errors[0])
    exit()
elif len(sys.argv) == 2:
    print(Errors[1])
    exit()
elif len(sys.argv) == 3:
    print(Errors[2])
    exit()


type = Arguments[1].lower()
Num1 = int(Arguments[2])
Num2 = int(Arguments[3])

if type == "add":
    print_answer(Add(Num1 , Num2))
elif type == "multiply":
    print_answer(Multiply(Num1 , Num2))
elif type == "divide":
    print_answer(Divide(Num1 , Num2))
elif type == "subtract":
    print_answer(Subtract(Num1 , Num2))
else:
    print("I dont know how to do that yet")
