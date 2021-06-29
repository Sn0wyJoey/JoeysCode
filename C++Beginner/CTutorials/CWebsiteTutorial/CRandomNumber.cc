#include <stdio.h> // printf, scanf, puts, NULL
#include <stdlib.h> // srand, rand
#include <time.h> // time

#include <iostream>
using namespace std;

int main(){
    int randomNum;
    srand(time(0)); //generates a pseudo-random number
    randomNum = (rand()%100+1); //assigns randomNum to a random number in between 1 and 100.
    cout << randomNum << endl; //prints the random number
}
