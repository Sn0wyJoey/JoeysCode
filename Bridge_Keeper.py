import colors as c
import time
def ask(question):
    answer_input = input(question + " >")
    lowercase_answer = answer_input.lower()
    return lowercase_answer
def die():
    print("You are cast into the gorge")
    exit()
def live():
    print(c.multi ("Right, off you go"))
    exit()
def Bridge_Keeper():
    print(c.red + "i- i dont know that!")
    time.sleep(1.5)
    print(c.red + "aaahhhhhh")
    exit()
#answer_name = input("What is your name?")
print(c.red + """
Who would cross the bridge of Death
 must answer these questions three
  'Ere the other side he see.
""")
time.sleep(2)
answer_name = ask(c.blue + "What is your name")
time.sleep(1)
answer_quest = ask("What is your quest?")
time.sleep(1.5)

if answer_name in ["lancelot" ,"galahad"]:
    answer_color = ask("What is your favorite color?")
    if answer_color in ["blue" ,"green"]:
        live()
    else:
        die()

elif answer_name == "robin":
    answer_capital = ask("What is the capital of Assyria")
    if answer_capital == "assur":
        live()
    else:
        die()

elif answer_name == "arthur":
    answer_velocity = ask("What is the airspeed velocity of a unlaiden swallow?")
    if answer_velocity in ["What do you mean, african or european?" , "african or european"]:
        Bridge_Keeper()
    elif answer_velocity in ["11mps", "eleven meters per second"]:
        live()
    else:  
        die()
else:
    die()
