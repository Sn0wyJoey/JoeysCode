#include <iostream>
using namespace std;

//we put void at the start of the function when we dont want our function to return any information.
void functionName(string name, int age){ //makes a function, there are perameters we can use in it.
    //one perameter accepts a string, so we can type in the string when calling the function. Same with the age parameter.
    cout << "Hello " << name;//this is what the function does
    cout << "!\n" << "You are " << age << " years old. You will be ";
    age += 10;
    cout << "\n" << age << " years old in 10 years.\n" << endl;

}

void hi(string word); //declares a function, but we can define it later after the main function.


int main(){
    functionName("Joey", 13); // we have to call the function to use it, and we can type in the string and age perameters to pass it in.
    functionName("Jake", 14);
    functionName("Jim", 15);
    hi("Hello world!");
}

void hi(string word){ // defines the function we declared earlier. We have to declare it early on so we can define it after the main function.
    cout << word;
}