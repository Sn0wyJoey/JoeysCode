import colors as c
import random as r
import time as t
def Has_Easter_Egg(Easter_Eggs , Question):
  for key in Easter_Eggs:
    if key in Question:
      return Easter_Eggs[key]

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
Easter_Eggs = {"love": "im not cupid" , "joey": "everything about joey is secret" , "death": "hey, we dont talk about death here."}
print(welcome + c.reset)
while True:
    Question = ask("What is your question?")
    Responces = ["yes" , "no" , "maybe" , "of course!" , "Of course not!" , "Ask again later" , "I dont know"]
    easter_egg = Has_Easter_Egg(Easter_Eggs , Question)
    if easter_egg:
      print(easter_egg)
    else:
      print(r.choice(Responces))
    Answer = ask("Want to ask another question?")
    if Answer not in ["yes" , "yea" , "ok" , "sure"]:
        break
print("Ok, Bye!")
t.sleep(1)

