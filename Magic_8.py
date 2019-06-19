import colors as c
import random as r
import time as t
def ask(question):
    answer_input = input(question + " >")
    lowercase_answer = answer_input.lower()
    return lowercase_answer
welcome = c.magenta + """

         _.-----._
      .-'         `-.
    .'     _..._     `.
   :     .' .-. `.     :
  :     :  :   :  :     :
 :      :  :   :  :      :
 :       `._`-'_.'       :
 :       .' .-. `.       :
 :      :  :   :  :      :
  :     :  :   :  :     :
   :     `._`-'_.'     :
    `.      '''      .'
      `-._       _.-'
          `-----'
""" 
print(welcome + c.reset)
while True:
    Question = ask("What is your question?")
    Responces = ["yes" , "no" , "maybe" , "of course!" , "Of course not!" , "Ask again later" , "I dont know"]
    print(r.choice(Responces))
    Answer = ask("Want to ask another question?")
    if Answer not in ["yes" , "yea" , "ok" , "sure"]:
        break
print("Ok, Bye!")
t.sleep(1)

