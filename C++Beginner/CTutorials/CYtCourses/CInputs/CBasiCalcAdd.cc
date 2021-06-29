#include <iostream>
using namespace std;

int main(){
    double num1, num2;
    //assigns these variables that the user will add
    cout << "Pick 2 numbers and I will add them.\nEnter the first number >";
    cin >> num1;
    //prompts the user to enter the first number and stores it in num1
    cout << "Now enter the second number >";
    cin >> num2;
    //prompts the user to enter the second number and stores it in num2
    cout << num1 + num2;
    //prints out the sum of the two numbers
}


/*Another solution:

int main(){
    double num1, num2, sum;
    cout << "Welcome to the calculator! Give us 2 numbers \nand we will calculate the sum." << endl;
    cout << "To start, enter the first number. >";
    cin >> num1;
    cout << "Now, enter the second number. >";
    cin >> num2;
    sum = num1 + num2;
    cout << num1 << " + " << num2 << " = " << sum << endl;
}  */

