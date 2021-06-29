class Solution {
public:
    int numberOfSteps(int num) {
    
    bool even, end;
    int steps;
    
    if(num == 0){
        end = true;
        steps = 0;
    } else {
        end = false;
    }
        
    while(end == false){
        if(num == 0){
            end = true;
        }
        if(num % 2 == 0){
            if(num == 0){
                steps--;
            }
            num /= 2;
            steps++;
        } else {
            num--;
            steps++;
            }
        }
    
    return steps;
    }
};