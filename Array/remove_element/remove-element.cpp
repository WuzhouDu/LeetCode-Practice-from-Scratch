class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int len = nums.size();
        int result = 0;
        vector<int> temp = *(new vector<int>(len));
        for (int i  = 0; i < len; i++){
            if (nums[i] != val){
                temp[result] = nums[i];
                result++;
            }
        }
        nums = temp;
        return result;
    }
};