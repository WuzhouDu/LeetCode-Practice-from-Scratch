class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;
        vector<int> result(right + 1);
        for (int i = left, j = right, m = right; i <= j; m--){
            if ((nums[i] + nums[j]) < 0){
                result[m] = nums[i]*nums[i];
                i++;
            }
            else{
                result[m] = nums[j]*nums[j];
                j--;
            }
        }
        return result;
    }
};