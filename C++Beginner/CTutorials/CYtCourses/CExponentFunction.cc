#include <iostream>
using namespace std;

//lets make something that makes 2 inputs from the user an exponent.

int exponent(int num, int powNum){
    int result = 1;

    for(int i = 0; i < powNum; i++ ){
        result = result * num;
    }
    return result;
}

int main(){
    cout << exponent(8, 2);

}