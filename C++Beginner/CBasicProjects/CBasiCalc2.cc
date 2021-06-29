#include <iostream>
using namespace std;

double findAdd(double num1, double num2){
    return num1 + num2;
}
double findSub(double num1, double num2){
    return num1 - num2;
}
double findMul(double num1, double num2){
    return num1 * num2;
}
double findDiv(double num1, double num2){
    return num1 / num2;
}

int main(){
    //startup pt 1
    cout << "\nLoading . . .";
    // loop
    bool loop = true;
    while (loop == true) {
        // startup pt 2
        cout << "\n" << "Welcome to the basic calculator!";
        
        // number 1
        double num1;
        cout << "\n" << "Enter your first number. >";
        cin >> num1;
        cout << "\n" << "First number: " << num1;

        // number 2
        double num2;
        cout << "\n" << "Now, enter your second number. >";
        cin >> num2;
        cout << "\n" << "Second number: " << num2;

        //shows selected numbers
        cout << "\n\n" << "These are your selected numbers:\n" << "First number: " << num1 << ".\n" << "Second number: " << num2;

        //operators
        int operator1; //use operator1 as variable name since operator is already something else.
        int operation;
        cout << "\n\nNow, to choose your operator:\n\nType 1 for Addition.\n\nType 2 for Subtraction.\n\nType 3 for Multiplication.\n\nType 4 for Division. \nTyping anything else will not work. >";
        cin >> operator1;
        
        //calling the functions
        if (operator1 == 1){
            double ansAdd;
            ansAdd = findAdd(num1, num2);
            cout << "\n" << num1 << " + " << num2 << " = " << ansAdd;
        } else if (operator1 == 2){
            double ansSub;
            ansSub = findSub(num1, num2);
            cout << "\n" << num1 << " - " << num2 << " = " << ansSub;
        } else if (operator1 == 3){
            double ansMul;
            ansMul = findMul(num1, num2);
            cout << "\n" << num1 << " * " << num2 << " = " << ansMul;
        } else if (operator1 == 4){
            double ansDiv;
            ansDiv = findDiv(num1, num2);
            cout << "\n" << num1 << " / " << num2 << " = " << ansDiv;
        } else {
            cout << "You have to put the correct number corresponding to the operator!\n\nTry again next time.";
        }
        //check if user wants to use this again
            int again;
            cout << "\n\nWould you like to go again?\nType 1 for yes.\n\nTyping anything else will exit the program >";
            cin >> again;
            if (again == 1){       
            } else {
                goto endLoop;
            }
        
    }
    endLoop: 
    cout << "\n\nGoodbye!";
}

