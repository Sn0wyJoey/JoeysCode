#include <iostream>

using namespace std;

int main(){
    string name;    
    double age;
    // makes the variables for the name and age
    cout << "Hello, what is your name? >";
    getline(cin, name);
    // asks for a string input and collects that input
    cout << "Welcome, " << name << "!" << endl;
    cout << "So " << name << ", how old are you? Enter your age number: >";
    // prints the input we entered, and asks us for a number input
    cin >> age;
    // collects the number input
    age += 10;
    cout << "Well, " << name << ". It looks like you will be " << age << " years old in 10 years." << endl;
    cout << "Goodbye " << name << "!";
}