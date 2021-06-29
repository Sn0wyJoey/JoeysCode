#include <iostream>
using namespace std;

int main(){
    int x = 1;
    double y;
    cout << "Pick a number >";
    cin >> y;
    while(x <= y){
        cout << x;
        x++;
    }

}