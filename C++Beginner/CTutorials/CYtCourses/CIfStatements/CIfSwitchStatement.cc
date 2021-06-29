#include <iostream>
using namespace std;

string DayofWeek(int dayNum){ //has a string at front because we want to return a string
    string dayName;
    switch(dayNum){
        case 0: // if dayNum == 0, then dayName = sunday
            dayName = "Sunday";
            break; //breaks out of case 0
        case 1:
            dayName = "Monday";
            break;
        case 2:
            dayName = "Tuesday";
            break;
        case 3:
            dayName = "Wednesday";
            break;
        case 4:
            dayName = "Thursday";
            break;
        case 5:
            dayName = "Friday";
            break;
        case 6:
            dayName = "Saturday";
            break;
        default: //if it is an invalid number.
            dayName = "Invalid Day Number"; 
    }
    return dayName;
}
int main(){
    cout << DayofWeek(10);
}