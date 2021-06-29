#include <iostream>
using namespace std;

int main(){
    int arrayName[] = {4, 8, 16, 32, 64, 128}; //makes an array of integers, the curly brackets store them.
    //                 0  1  2   3   4   5
    // index positions start at 0.
    cout << arrayName[0] << endl;// prints the first number 4 in the array

    arrayName[0] = 5; //modifies the first element in the array (they are called elements)
    cout << arrayName[0] << endl;
    //now when I print the first element of the array, we print the changed thing: 5.

    //new array

    int arrayName2[20] = {5, 10, 15, 20, 25, 30};
    // by entering 20, we are telling the array that we want 20 elements in it. This puts a max number 
    // so we can put in numbers later. 

    //we can add elements in the array
    arrayName2[10] = 55; //makes the 10th position in the array equal to 55.
    cout << arrayName2[10]; //prints the 10th element in the array so it will print 55.

    //new array

    int array3[20] = {}; 
    //sometimes we dont know whats going to be in the array when we make it, so we can change what is in it later and
    //leave it empty for now.

    array3[0] = 10; //changes the first element of the array to 10
    cout << "\n" << array3[0];

}