#include <iostream>
#include <cmath> //do this for more math functions.

using namespace std;

int main(){
    cout << -40.234 << endl; //prints this number.
    cout << 5 + 7 << endl; //prints the sum of the 2 numbers
    cout << 5 - 7 << endl; //prints the difference of the 2 numbers
    cout << 5 * 7 << endl; //prints the product of the 2 numbers
    cout << 5 / 7 << endl; //prints the quotient of the 2 numbers
    cout << 10 % 3 << endl; //prints the modulus, (remainder of 10/3)
    
    int num = 5; //stores WHOLE numbers
    double dnum = 5.234; //stores decimal numbers
    
    num++; //adds 1 to num, so it is 6 (num+1)
    num--; //subtracts 1 from num, so it is 5 (num-1)
    num += 80; //adds 80 to num so it is 85 (num+80)
    num -= 80; //subtracts 80 from num so it is 5 (num-80)
    num *= 5; //multiplies num by 5 so it is 25 (num*5)
    num /= 5; //divides num by 5 so it is 5 (num/5)
    cout << num << endl; //prints num

    //when you do math with a whole number and a decimal number, you will get the decimal number back.
    //when you do math with 2 integers, you will get an integer value back, so its bad for dividing.
 
    // #include <cmath> functions
    
    //pow, (power of) takes 2 arguments and does the first argument to the power of the second one.
 
    cout << pow(2,5) << endl; //does 2^5 (2 to the power of 5)
    
    //square root
    cout << sqrt(34) << endl; // does the square root of 34 

    //round
    cout << round(3.6) << endl; //rounds to the nearest whole number
 
    //ceil
    cout <<  ceil(4.1) << endl; //rounds the number up
    //so it would be 5

    //floor
    cout << floor(3.6) << endl; //rounds the number down
    //so it would be 3

    //fmax
    cout << fmax(3, 10) << endl; //returns the bigger number
    //so it would be 10

    //fmin
    cout << fmin(3, 4) << endl; //returns the smaller number
    //so it would be 3

}