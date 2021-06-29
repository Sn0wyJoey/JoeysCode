#include <iostream>
using namespace std;


int main(){

    int numberGrid[3][2] = { 
                            {1, 2},     
                            {3, 4},
                            {5, 6}
    };
    //lets loop through all of the elements in this array.

    for(int i = 0; i < 3; i++){/*we use < 3 because we want to loop th
        for each of the elements in the array, we also want to loop through the elements inside of the elements, so lets create another for loop. */
        for(int j = 0; j < 2; j++){
            cout << numberGrid[i][j] << endl;
        }
    } //loops through numberGrid.

}  
