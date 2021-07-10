import colors as c
import random as r
import time as t

def ask(question):
    answer_input = input(question + "> ")
    lowercase_answer = answer_input.lower()
    return lowercase_answer
def win(a,b):
    if (a == "rock" and b == "scissors") \
    or (a == "paper" and b == "rock") \
    or (a == "scissors" and b == "paper"):
        return True
    else:
        return False

Space = (" >")
print("Lets play rock paper scissors!")
Ai_Wins = 0
Player_Wins = 0
try:
    while True:
        Responce = ask("Do you choose Rock, Paper, or Scissors?" + Space)
        Rps = ["rock", "paper", "scissors"]
        while Responce not in Rps:
            Responce = ask("Do you choose Rock, Paper, or Scissors?" + Space)
        Ai = (r.choice(Rps))
        t.sleep(1)
        if win(Ai , Responce):
            Ai_Wins += 1 
            print(c.bright_red + "You Lost" + c.clear)
            print("I had " + Ai)
        elif win(Responce,Ai):
            Player_Wins += 1
            print(c.bright_green + "You won!" + c.clear)
            print("I had " + Ai)
        else:
            print(c.bright_yellow + "We tied!" + c.clear)
        print("Ai " , Ai_Wins)
        print("You " , Player_Wins)
        Again = ask("Want to go again?" + Space)
        if Again in ["yes" , "yea" , "ok" , "sure"]:
            pass
        else:
            break
    print(c.bright_blue + "Ok, Bye!" + c.clear)
    exit()
except KeyboardInterrupt:
    print(c.bright_blue + '\nGoodbye!' + c.clear)