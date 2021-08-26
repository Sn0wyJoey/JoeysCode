import random as r
import colors as c
from hangmanboards import *

def getBoard(Lives):
    if Lives == 6:
        return Board5
    elif Lives == 5:
        return Board5
    elif Lives == 4:
        return Board4
    elif Lives == 3:
        return Board3
    elif Lives == 2:
        return Board2
    else:
        return Board1

def getWord():
    file = open('./Passwords/Words.txt', 'r')
    lines = file.readlines()
    word = r.choice(lines).replace('\n', '', -1)
    for i in range(len(word)):
        List_Word.append(word[i].upper())
        test.append(word[i].upper())
        Guess_Word.append('_')
    return word
#----------------------------------------------------------------------------------------------------
def checkAns(ask, Lives, history):
    for i in range(len(List_Word)):
        if ask in List_Word[i]:
            if ask in history and ask not in List_Word:
                print(c.red + '\n\nYou already used that letter!' + c.reset)
                return False
            Guess_Word[i] = List_Word[i].upper()
            List_Word.remove(ask)
            List_Word.insert(i, "None")
            return True

while True:
    List_Word, Guess_Word, history, test = [], [], [], []
    end, lives = False, 6
    x = getWord()
    print('\n' + Board5 + '\n\n' + str(Guess_Word) + ' Lives left: ' + str(lives-1) + '\n')
    while end == False:
        # Ask for letter input
        ask = str(input(c.magenta + 'Enter a letter you think is in the word: ').upper())
        print(List_Word)

        # Checks if the letter is in the list and adds the letter to the history
        if checkAns(ask, lives, history) == True:
            print(c.green + '\nCorrect!' + c.reset)
        else:
            print(c.red + '\nWrong!' + c.reset)
            lives -= 1
        history.append(ask)

        # Print the board, lives left,  and history.
        print('\n' + getBoard(lives) + '\n\n' + str(Guess_Word) + ' Lives left: ' + str(lives-1) + '\n' + 'Letters used: ' + str(history) + '\n')

        # Check if game is over yet and see if they won
        if lives == 1:
            end = True
            print(c.bold + c.red + 'You Lost!' + c.reset)
            print(f'The word was \'{c.red + x + c.reset}\'!')
        elif test == Guess_Word:
            end = True
            print(c.bold + c.green + 'You Won!' + c.reset)
    
    # Ask if user wants to go again, and loops back if they do, else break out of the while loop.
    again = str(input('Do you want to go again? (y/n): ').lower())
    if again == 'y':
        pass
    else:
        break

print('Goodbye!')
   