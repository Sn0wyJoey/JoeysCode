import colors as c
import random as r
def ask(question):
    answer_input = input(question + " >")
    lowercase_answer = answer_input.lower()
    return lowercase_answer
File = open("Words.txt" , "r")
Lines = File.readlines()
print("Welcome to Random Password Picker!")
while True:
    Noun = r.choice(Lines).replace("\n" , "",-1)
    Num = [1, 2 ,3 ,4 ,5 ,6 ,7, 8 , 9, 0]
    Special = ["!" , "@" , "#" , "$" , "%" , "^" , "&" , "*" ,]
    RSpecial = r.choice(Special)
    RNum = str(r.choice(Num))
    Shuffle = [RNum , RSpecial, Noun]
    r.shuffle(Shuffle)
    print("Here is your password!" , "".join(Shuffle))
    Another = ask("Do you want another password?")
    if Another in ["yes" , "sure" , "ok" , "yea"]:
        pass
    else:
        break
print("Thank You for using Random Password Picker!")

