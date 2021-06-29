class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        
        vector<int> result;
        int below = 0;

        for(int i = 0;  i < nums.size(); i++){
            below = 0;
            for(int j = 0; j < nums.size(); j++){
                if(nums[i] > nums[j] && nums[i] != nums[j]){
                    below = below + 1;
                }
            }
            result.push_back(below);
        }
        return result;
    }
};