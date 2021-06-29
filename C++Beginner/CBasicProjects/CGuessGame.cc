#include <iostream>
#include <stdio.h> // printf, scanf, puts, NULL
#include <stdlib.h> // srand, rand
#include <time.h> // time
using namespace std;
//make a guessing game, where the user has to guess a secret number.

void easy(){ /*easy mode, number has 5 number range. User gets 4 guesses
    declares some variables */
    int secretNum, guess1, guess2, guess3, guess4, again;

    //makes random number
    easyStart:
    srand(time(0));
    secretNum = (rand()%100+1);
    //helps decide to subract the secret num by subtracting 2 or 3 and add by 2 or 3 so we can say the secret number is in between x and y
    int randomRange;
    randomRange = (rand()%2+1);
    
    //guess 1 and hint
    cout << "\nThe secret number has been generated. You will get 4 guesses. The secret number is in between "; 
    
    //helps decide to subract the secret num by subtracting 2 or 3 and add by 2 or 3 so we can say the secret number is in between x and y
    switch(randomRange){
        case 1:
            cout << secretNum - 2 << " and " << secretNum + 3;
            break;
        
        case 2:
            cout << secretNum - 3 << " and " << secretNum + 2;
            break;
    }
    cout << ".\nHave you thought of the number? Type it here >>>";
    cin >> guess1;

    //checks if first guess is correct. This will be repeated.
    if (guess1 == secretNum){
        cout << "\n\nYou are correct! Congratulations, you won! Do you want to play again?\nPress 1 for yes, and anything else for no. >>>";
        cin >> again;
        if (again == 1) {
            goto easyStart; 
        } else {
            goto easyEnd;
        }
    } else {
        cout << "\n\nSorry, you are incorrect. You have 3 more guesses.";
        goto secondGuess;
    }
    
    //guess 2
    secondGuess:
    cout << "\nThis is your second guess. Have you thought of the number? Type it here >>>";
    cin >> guess2;
    
    if (guess2 == secretNum){
        cout << "\n\nYou are correct! Congratulations, you won! Do you want to play again?\nPress 1 for yes, and anything else for no. >>>";
        cin >> again;
        if (again == 1) {
            goto easyStart; 
        } else {
            goto easyEnd;
        }
    } else {
        cout << "\n\nSorry, you are incorrect. You have 2 more guesses.";
        goto thirdGuess;
    }
    
    //guess 3
    thirdGuess:
    cout << "\nThis is your third guess. Have you thought of the number? Type it here >>>";
    cin >> guess3;
    
    if (guess3 == secretNum){
        cout << "\n\nYou are correct! Congratulations, you won! Do you want to play again?\nPress 1 for yes, and anything else for no. >>>";
        cin >> again;
        if (again == 1) {
            goto easyStart; 
        } else {
            goto easyEnd;
        }
    } else {
        cout << "\n\nSorry, you are incorrect. You have 1 more guesses.";
        goto fourthGuess;
    }

    //guess 4
    fourthGuess:
    cout << "\nThis is your last guess. Have you thought of the number? Type it here >>>";
    cin >> guess4;
    
    if (guess4 == secretNum){
        cout << "\n\nYou are correct! Congratulations, you won! Do you want to play again?\nPress 1 for yes, and anything else for no. >>>";
        cin >> again;
        if (again == 1) {
            goto easyStart; 
        } else {
            goto easyEnd;
        }
    } else {
        cout << "\n\nSorry, you are incorrect. You have no more guesses.\nThe answer was " << secretNum << ".\nDo you want to play again?\nPress 1 for yes, and anything else for no. >>>";;
        cin >> again;
        if (again == 1) {
            goto easyStart; 
        } else {
            goto easyEnd;
        }
    }

    easyEnd:
    cout << "\nGoodbye!";
    exit(0);
}






void medium(){ //medium mode, number has 10 number range. User gets 4 guesses
    //declares some variables
    int secretNum, guess1, guess2, guess3, guess4, again;

    //makes random number
    midStart:
    srand(time(0));
    secretNum = (rand()%500+1);
    
    //guess 1 and hint
    cout << "\nThe secret number has been generated. You will get 4 guesses. The secret number is in between " << secretNum - 5 << " and " << secretNum + 5 << ".\nHave you thought of the number? Type it here >>>";
    cin >> guess1;

    //checks if first guess is correct. This will be repeated.
    if (guess1 == secretNum){
        cout << "\n\nYou are correct! Congratulations, you won! Do you want to play again?\nPress 1 for yes, and anything else for no. >>>";
        cin >> again;
        if (again == 1) {
            goto midStart; 
        } else {
            goto midEnd;
        }
    } else {
        cout << "\n\nSorry, you are incorrect. You have 3 more guesses.";
        goto secondGuess;
    }
    
    //guess 2
    secondGuess:
    cout << "\nThis is your second guess. Have you thought of the number? Type it here >>>";
    cin >> guess2;
    
    if (guess2 == secretNum){
        cout << "\n\nYou are correct! Congratulations, you won! Do you want to play again?\nPress 1 for yes, and anything else for no. >>>";
        cin >> again;
        if (again == 1) {
            goto midStart; 
        } else {
            goto midEnd;
        }
    } else {
        cout << "\n\nSorry, you are incorrect. You have 2 more guesses.";
        goto thirdGuess;
    }
    
    //guess 3
    thirdGuess:
    cout << "\nThis is your third guess. Have you thought of the number? Type it here >>>";
    cin >> guess3;
    
    if (guess3 == secretNum){
        cout << "\n\nYou are correct! Congratulations, you won! Do you want to play again?\nPress 1 for yes, and anything else for no. >>>";
        cin >> again;
        if (again == 1) {
            goto midStart; 
        } else {
            goto midEnd;
        }
    } else {
        cout << "\n\nSorry, you are incorrect. You have 1 more guesses.";
        goto fourthGuess;
    }

    //guess 4
    fourthGuess:
    cout << "\nThis is your last guess. Have you thought of the number? Type it here >>>";
    cin >> guess4;
    
    if (guess4 == secretNum){
        cout << "\n\nYou are correct! Congratulations, you won! Do you want to play again?\nPress 1 for yes, and anything else for no. >>>";
        cin >> again;
        if (again == 1) {
            goto midStart; 
        } else {
            goto midEnd;
        }
    } else {
        cout << "\n\nSorry, you are incorrect. You have no more guesses.\nThe answer was " << secretNum << ".\nDo you want to play again?\nPress 1 for yes, and anything else for no. >>>";;
        cin >> again;
        if (again == 1) {
            goto midStart; 
        } else {
            goto midEnd;
        }
    }

    midEnd:
    cout << "\nGoodbye!";
    exit(0);
}





void hard(){ //hard mode, number has 10 number range. User gets 1 guess
    //declares some variables
    int secretNum, guess1, again;

    //makes random number
    hardStart:
    srand(time(0));
    secretNum = (rand()%5000+1);
    
    //guess 1 and hint
    cout << "\nThe secret number has been generated. You will get 1 guess. The secret number is in between " << secretNum - 5 << " and " << secretNum + 5 << ".\nHave you thought of the number? Type it here >>>";
    cin >> guess1;
    
    if (guess1 == secretNum){
        cout << "\n\nYou are correct! Congratulations, you won! Do you want to play again?\nPress 1 for yes, and anything else for no. >>>";
        cin >> again;
        if (again == 1) {
            goto hardStart; 
        } else {
            goto hardStart;
        }
    } else {
        cout << "\n\nSorry, you are incorrect. You have no more guesses.\nThe answer was " << secretNum << ".\nDo you want to play again?\nPress 1 for yes, and anything else for no. >>>";;
        cin >> again;
        if (again == 1) {
            goto hardStart; 
        } else {
            goto hardEnd;
        }
    }

    hardEnd:
    cout << "\nGoodbye!";
    exit(0);
}











int main(){
    //declaring variales
    int diffLevel, redo;
    string name;
    
    //startup 
    Name:
    cout << "Hello! Welcome to the Guessing game! Do you have a name? >>>My name is: ";
    cin >> name;
    
    Start:
    //decide difficulty
    cout << "\nOk, " << name << "! Lets pick a difficulty.\n\nPress 1 for Easy\nPress 2 for Medium\nPress 3 for Hard\n\nWarning: Typing anything else will not work.\nGamemode difficulty: ";
    cin >> diffLevel;
    
    //call functions depending on difficulty
    switch (diffLevel){
        case 1:
            Easy:
            cout << "\nDifficulty: Easy" << endl;
            easy();
            break;
        case 2:
            Medium:
            cout << "\nDifficulty: Medium" << endl;
            medium();
            break;
        case 3:
            Hard: 
            cout << "\nDifficulty: Hard" << endl;
            hard();
            break;
        default: 
            cout << "\nERROR: Invalid level. Read the instructions and try again.\n\nDo you want to try again?\nPress 1 for yes.\nPress anything else for no. >>>";
            cin >> redo;
            if (redo == 1){
                goto Start;
            } else {
                goto End;
            }

             
    }
     




    //end
    End:
    cout << "\nGoodbye, read the instructions next time.";
}