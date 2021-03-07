secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        out_of_guesses = False
        guess = input("Enter guess here > ")
        guess_count += 1
    else:
        out_of_guesses = True
        
if out_of_guesses == True:
    print("Out of guesses, GAME OVER")
else:
    print("You Win!")
