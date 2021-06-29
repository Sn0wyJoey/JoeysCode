  #include <iostream>
using namespace std;

void hard(){ 
    //declares some variables
    int secretNum, guess1, again;

    //makes random number
    hardStart:
    srand(time(0));
    secretNum = (rand()%5000+1);
    
    //guess 1
    redo:
    cout << "You will get unlimited guesses.\nHave you thought of the number? Type it here >>>";
    cin >> guess1;
    
    if (guess1 == secretNum){
        cout << "\n\nYou are correct! Congratulations, you won! Do you want to play again?\nPress 1 for yes, and anything else for no. >>>";
        cin >> again;
        if (again == 1) {
            goto hardStart; 
        } else {
            goto hardEnd;
        }
    } else {
        cout << "\n\nSorry, you are incorrect.";
        if (guess1 < secretNum){
            cout << "\nThe secret number is HIGHER than what you entered.";
            goto redo;
        } else {
            cout << "\nThe secret number is LOWER than what you entered.";
            goto redo;
        }
    }
   

    hardEnd:
    cout << "\nGoodbye!";
    exit(0);
}

int main(){
    hard();
}