class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int end = 0;
        int sum = nums[0];
        int result = 0;
        for (int i = 0; i < nums.size(); i++){
            if (i != 0){
                sum -= nums[i-1];
            }
            while (sum < target){
                end++;
                if (end >= nums.size()) return result;
                sum += nums[end];
            }
            if (result == 0) result = end - i + 1;
            else if (end - i + 1 < result) result = end - i + 1;
        }
        return result;
    }
};