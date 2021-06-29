#include <iostream>
using namespace std;

int main(){
    bool isTrue = false;
    bool isGood = true;

    if(isTrue && isGood){  //what if we wanted to check if it was true but NOT good? We use else if.    
        cout << "It is good and true";
    } else if (isTrue && !isGood){  //we want to check if it is true but NOT good, so we put an exclamation point in front of isGood. Its called the negation operator.
    // ^ is basically saying else if is true and NOT good.
    // this is the else if. If the condition on top of this is false, it goes here. If this condition is false, it goes to the bottom. Its like python elif. 
        cout << "It is true, but not good"; 
    } else if (!isTrue && isGood){ //if it is NOT true but good
        cout << "It is good, but not true.";
    } 
        else { // if it is bad and not true.
        cout << "It is not good and false.";
    }
}