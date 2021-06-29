class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        
        int result = 0, x = 0;
        vector<int> big;
        
        for(int i = 0; i < accounts.size(); i++){
            x = accounts[i][0];
            for(int j = 1; j < accounts[i].size(); j++){
                x = x + accounts[i][j];
            }
            big.push_back(x);
        }
        
        for(int k = 0; k < big.size(); k++){
            if(result <= big[k]){
                result = big[k];
            }
        }
        
    return result;
    }
};