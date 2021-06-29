#include <iostream>
using namespace std;

double getmax(double num1, double num2, double num3){
    double largerNum;
    
    if (num1 >= num2 && num1 >= num3){ //if num1 is greater than or equal to num2 and num1 is greater than or equal to num3
        largerNum = num1;
    } else if (num2 >= num1 && num2 >= num3){
        largerNum = num2;
    } else {
        largerNum = num3;
    }
    return largerNum;
    //this function returns the largest number of 3 numbers.
} 

int main(){
    double bigNum;
    bigNum = getmax(4.5, 10.6745, 10.6745);
    cout << "The largest number is " << bigNum;
}