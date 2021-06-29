#include <iostream>
using namespace std;

int main(){
    bool isTrue = true;
    bool isGood = true;

    if(isTrue && isGood){     //to check if isTrue and isGood are both true, we can do the && (and operator) 
        cout << "It is good and true";
        //ONLY if isTrue and isGood are true, then we print it.
    } else {
        cout << "It is false";
        //if 1 is true and the other is false or both are false, then we print this instead.
    }
}