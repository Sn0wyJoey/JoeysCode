#include<iostream>

using namespace std;
//this is for getting inputs from users that are characters or numbers.
int main(){
    double age; //assigns an integer to variable age, we will let the user decide the value
    cout << "Enter your age: "; //tells them to enter a number
    cin >> age; /*cin gets information, also put >> instead of <<.
      ^ after typing cin >>, type the variable you want to store the information in. */
    cout << "You are " << age << " years old." << endl;
    age += 5; //adds 5 to age so we can tell the age in 5 years
    cout << "You will be " << age << " years old in 5 years.";





}