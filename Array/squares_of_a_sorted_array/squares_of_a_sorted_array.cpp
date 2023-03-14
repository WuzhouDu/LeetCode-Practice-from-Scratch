class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int len = nums.size();
        int left = 0;
        int right = len-1;
        int zero_index;
        int middle;
        vector<int> result(len);

        if (nums[len-1]<=0){
            for (int i = 0; i < len;i++){
                result[i] = nums[len - i - 1]*nums[len - i - 1];
            }
            return result;
        }
        else if (nums[0] >= 0){
            for (int i = 0; i < len;i++){
                result[i] = nums[i]*nums[i];
            }
            return result;
        }
        


        while (left <= right){
            middle = left + (right - left) / 2;
            if (nums[middle] > 0){
                right = middle - 1;
            }
            else if (nums[middle] < 0){
                left = middle + 1;
            }
            else{
                break;
            }
        }
        zero_index = middle;


        if (nums[middle] > 0) zero_index--;
        int left_ptr = zero_index;
        int right_ptr = zero_index + 1;
        for (int i = 0; i < len; i++){
            if (left_ptr < 0){
                result[i] = nums[right_ptr]*nums[right_ptr];
                right_ptr++;
            }
            else if (right_ptr > len - 1){
                result[i] = nums[left_ptr]*nums[left_ptr];
                left_ptr--;
            }
            else if (nums[left_ptr] + nums[right_ptr] <= 0){
                result[i] = (nums[right_ptr])*(nums[right_ptr]);
                right_ptr++;
            }
            else{
                result[i] = (nums[left_ptr])*(nums[left_ptr]);
                left_ptr--;
            }
        }
        return result;
    }
};