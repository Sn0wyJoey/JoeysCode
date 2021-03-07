def tran(phrase):
    tra = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                tra = tra + "J"
            else:
                tra = tra + "j"
        else:
            tra = tra + letter
    return tra

while True:
    print(tran(input("Enter a phrase > ")))
    again = input("Do you want to go again? Type yes to go again and type anything else to exit. > ")
    if again.lower() in ["yes" , "yea" , "of course" , "of course!" , "yes!" , "yea!"]:
        pass
    else:
        break

print("Thanks for using the translator!")
exit()


