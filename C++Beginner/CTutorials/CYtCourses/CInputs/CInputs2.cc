#include <iostream>

using namespace std;
//this is getting inputs from users that are strings
int main(){
    string name; //makes a variable, but we dont define it because we want the user to define it.
    cout << "Enter your name: ";  //asks the user to enter a string.
    getline(cin, name); //this is for getting strings from user input.
    /* the cin in the first perameter is the command prompt we enter stuff in. The second perameter (name)
     is the variable we store it in. */
    cout << "Hello " << name << "!" << endl;


}