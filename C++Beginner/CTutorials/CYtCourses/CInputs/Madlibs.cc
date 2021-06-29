#include <iostream>
using namespace std;

int main(){
    string name, pnoun, cel, color; //adds the variables
    cout << "Welcome to Madlibs! What is your name? >";
    getline(cin, name);
    cout << "Hello, " << name << "! Enter in a few words and I will create a\nstory including them.\nEnter a plural noun. >";
    getline(cin, pnoun);
    cout << "Enter a celebrity >";
    getline(cin, cel);
    cout << "Enter a color >";
    getline(cin, color);
    //welcomes the user and asks for other stuff like plural nouns, celebrities, colors, and a name to put in variables.
    cout << "\nRoses are " << color << ",\n" << pnoun << " are too,\nand so is " << cel << "." << endl;
    cout << "Goodbye " << name << "!";
    //prints a story including the variables, and says goodbye to the name variable.
}