#include <iostream>
using namespace std;

int main(){
    int index = 1;
    while(index <= 5){
        index++;
        //do stuff 5 times
    }
    
    //now for a for loop,

    for(int i = 1; i <= 5; i++){ /*for the first perameter, we declare a variable right INSIDE the for loop.
                            for the second perameter, while it is true, we use the loop. (looping condition, so while i <= 5, we do stuff.)
                            for the third perameter, we put index++ so it adds 1 to index after each round, so that we can reach the looping condition for the second perameter. */
        cout << i << endl;

    }



}