class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int len = nums.size();
        if (len == 1) return 1;
        int slow = 0;
        for (int fast = 0; fast < len; fast++){
            if (nums[fast] > nums[slow]){
                nums[++slow] = nums[fast];
            }
        }
        return slow+1;
    }
};