#include <iostream>
using namespace std;

int main()
{   // the endl at the end is what ends the line, so if you remove it,
    cout << "Hello"; //it will print the next line with endl in the same line as the first one.
    cout << " World" << endl; // putting \n at the end will do what endl does;
    cout << "Goodbye\n"; //put it in a new line.
    cout << "World" << endl;

    string phrase = "Hi";
    cout << phrase << endl; // prints the variable phrase

    //string functions
    string word = "Hello!";

    //length function, tells the amount of characters in a string.
    cout << word.length() << endl; // calls the function
    
    // accessing the characters in a string:
    cout << word[0] << endl; // 0 is the first character in a string.
    // accesses the first character.
    cout << word[3] << endl; // accesses the 4th character, they start from 0 when indexing a string.

    //modify an individual character in a string
    word[2] = 'e';  // changes the 3rd character to "e" instead of the original "l"
    cout << word << endl; //prints the modified string.
    
    //find, finds out if a specific thing is in a string
    cout << word.find("Heelo", 0) << endl; //finds out if Heelo is in the string.
    // the second perameter is the index where you want to start looking. If you want to check if it is in the string, put 0.
    //if you want to see if it occured after the 3rd index, put 3. It will give a number which is the position inside of the string
    //where "heelo" occurs.

    //substr, allows us to get a part of a string.(substring)
    //takes 2 perameters. The first one is the starting index of what you want to get.
    //so if I wanted to take all the characters after the first e, I will take all the characters from the 1st index (2nd character) and type in 1
    //the second one is how many characters I want to grab. If I want to get 'eel', then that is 3 characters, so I type in 3.
    cout << word.substr(1, 3) << endl; //gets "eel" from "heelo"
    string wordsub; //we can make the part we get into another string variable
    wordsub = word.substr(1, 3); //makes the eel part into a string
    cout << wordsub << endl; //prints the new string 'eel
    }

