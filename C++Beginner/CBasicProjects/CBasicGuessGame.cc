#include <iostream>
#include <stdio.h> // printf, scanf
#include <stdlib.h> // srand, rand
#include <time.h> // time
using namespace std; 

int main(){
    srand(time(0));
    int secretNum = (rand()%10+1), guesses = 0, guess;
    
    do {
        cout << "Enter your guess, you have 3 turns. It is a whole number between 1 and 10. > ";
        cin >> guess;
        guesses++;
      } while (secretNum != guess && guesses < 3);
    
    if(guess == secretNum) {
        cout << "\nYou won! Congrats!";
    } else {
        cout << "\nYou lost";
    }   
}