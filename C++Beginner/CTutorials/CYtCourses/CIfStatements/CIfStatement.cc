#include <iostream>
using namespace std;

int main(){
    //bool variable stores a true or false
    bool isTrue = true;
    // if the condition inside the parenthesis is true, we will do what is in the brackets. If it is false, we will move on, unless theere is an else.
    
    if(isTrue){
        cout << "It is true"; //prints if the condition is true
    } else { // The else statement also has brackets, and will only be run if the condition is false.
        cout << "It is false"; //prints if the condition is false
    } 
}