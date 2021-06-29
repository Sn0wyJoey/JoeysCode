class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        
        vector<int> result;
        int num = nums[0]; result.push_back(num);
        
        for(int i = 1; i < nums.size(); i++){
            num = num + nums[i]; 
            result.push_back(num);
        }
        
        return result;
        
    }
};