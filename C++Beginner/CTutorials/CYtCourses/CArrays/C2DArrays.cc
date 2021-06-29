#include <iostream>
using namespace std;

int main(){
    //2D array is an array where every element in an array is an array.
    //to do one, do an array with 2 "[]"

    int numberGrid[3][2] = {       //the first "[]" (perameter) is how many elements you want in the 2d array. The second "[]" (perameter) is how many elements you want in each element.
                            {1, 2}, //first element
                            {3, 4},
                            {5, 6}
    };

    //now lets access some elements.
    
    int x, y;
    cout << "Access element: ";
    cin >> x;
    
    cout << "Access element inside element: ";
    cin >> y;
    cout << numberGrid[x][y]; //the first perameter is which row you want to access, or which first element you want to access.
                             //the second perameter is the column you want to access, or which element inside the first element you want to access.

} //you can get more than 2d arrays, like 5d and 10d arrays.