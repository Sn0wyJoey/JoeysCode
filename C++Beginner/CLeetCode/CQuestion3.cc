class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        
        int biggestNum = 0;
        vector<bool> x;
        
        for(int i = 0; i < candies.size(); i++){
            if (biggestNum <= candies[i]){
                biggestNum = candies[i];
            }     
        }
        
        for(int j = 0; j < candies.size(); j++){
            if (candies[j] + extraCandies >= biggestNum){
                x.push_back(true);  
            } else {
                x.push_back(false);
            }
            
        }
        
        return x;
        
        
    }
};