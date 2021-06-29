#include <iostream>
using namespace std;

int main(){
    bool isTrue = true;
    bool isGood = false;
    
    if(isTrue || isGood){     //using || (or operator), only one of the conditions has to be true in order for the if code to execute.
        cout << "It is good and/or true";
        //if only 1 or both are true, then it will print.
    } else {
        cout << "It is false";
        //if none are true, then we print this.
    }
}
