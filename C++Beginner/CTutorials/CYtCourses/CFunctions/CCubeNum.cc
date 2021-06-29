#include <iostream>
using namespace std;

//instead of putting void, we want to return something in this function, so we have to put the data type we are returning in the front of the function (like strings, char, int, doubles, etc.)
//we want to cube a number, so we should do a double since that is what we will return.
double cube(double num){
    double cubed = num * num * num; // cubes num
    return cubed; //returns the value called cubed 
}

double shorterCube(double num); //it has a double at the front because we want to return a double

int main(){
    cube(5); // if we do this, it will find the number but it won't print anything.

    double result = cube(6.5); //the returned value from the cube function will get stored inside of the result variable.
    cout << result << endl;

    cout << shorterCube(3); //we can also print out the cube value alone without the variable.
}

double shorterCube(double num){
    return num * num * num; //we can also return the num cubed itself.
    cout << "Hello"; // it wont print hello because we already returned the function.
}