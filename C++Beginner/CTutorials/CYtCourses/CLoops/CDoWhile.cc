#include <iostream>
using namespace std;

int main(){
    int x = 6;
    do{ //the "do" is like a while loop but instead of checking the condition and then continuing, it does the stuff and then checks the condition after the stuff it does to see if it should loop back so it can do it at least once.
        cout << x << endl;
        x++;
    } while(x <= 0); 
} 