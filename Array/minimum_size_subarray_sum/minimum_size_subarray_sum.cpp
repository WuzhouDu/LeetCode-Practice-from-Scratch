class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int sum_of_all;
        for (int i = 0; i < nums.size(); i++){
            sum_of_all += nums[i];
        }
        
        if (sum_of_all < target) return 0;

        int result = nums.size();

        for (int i = 0, j = nums.size()-1; i <= j;){
            if (nums[i] < nums[j]){
                i++;
                sum_of_all -= nums[i];
            }
            else {
                j--;
                sum_of_all -= nums[j];
            }
            if (sum_of_all < target) return result;
            else result--;
        }
        return result;
    }
};