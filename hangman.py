import random as r
import colors as c

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
    file = open('hangman.txt', 'r')
    lines = file.readlines()
    word = r.choice(lines).replace('\n', '', -1)
    for i in range(len(word)):
        List_Word.append(word[i].upper())
        Guess_Word.append('_')
    return word

def checkAns(ask, Lives):
    for i in range(len(List_Word)):
        if ask in List_Word[i]:
            Guess_Word[i] = List_Word[i].upper()
            return True

Board5 = """       _______
     |/      |
     |     
     |     
     |         
     |      
     |
    _|___"""

Board4 = """       _______
     |/      |
     |      (_)
     |     
     |         
     |      
     |
    _|___"""

Board3 = """       _______
     |/      |
     |      (_)
     |       |
     |       |    
     |      
     |
    _|___"""

Board2 = """       _______
     |/      |
     |      (_)
     |      \|/
     |       | 
     |      
     |
    _|___"""

Board1 = """       _______
     |/      |
     |      (_)
     |      \|/
     |       |    
     |      / \\
     |
    _|___"""

while True:
    List_Word, Guess_Word = [], []
    end, lives = False, 6
    x = getWord()
    print('\n' + Board5 + '\n\n' + str(Guess_Word) + ' Lives left: ' + str(lives-1) + '\n')
    while end == False:
        # Ask for letter input
        ask = str(input(c.magenta + 'Enter a letter you think is in the word: ').upper())

        # Checks if the letter is in the list
        if checkAns(ask, lives) == True:
            print(c.green + '\nCorrect!' + c.reset)
        else:
            print(c.red + '\nWrong!' + c.reset)
            lives -= 1

        # Print the board and lives left
        print('\n' + getBoard(lives) + '\n\n' + str(Guess_Word) + ' Lives left: ' + str(lives-1) + '\n')

        # Check if game is over yet and see if they won
        if lives == 1:
            end = True
            print(c.bold + c.red + 'You Lost!' + c.reset)
            print(f'The word was \'{c.red + x + c.reset}\'!')
        elif List_Word == Guess_Word:
            end = True
            print(c.bold + c.green + 'You Won!' + c.reset)
    
    # Ask if user wants to go again, and loops back if they do, else break out of the while loop.
    again = str(input('Do you want to go again? (y/n): ').lower())
    if again == 'y':
        pass
    else:
        break

print('Goodbye!')
   