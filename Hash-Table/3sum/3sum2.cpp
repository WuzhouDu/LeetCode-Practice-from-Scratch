class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 2; i++){
            if (i > 0 && nums[i-1] == nums[i]){
                continue;
            }
            int left = i + 1;
            int right = nums.size() - 1;
            while (left < right){
                // cout << nums[i] << nums[left] << nums[right] << endl;
                if (nums[i] + nums[left] + nums[right] > 0){
                    right--;
                }
                else if (nums[i] + nums[left] + nums[right] < 0){
                    left++;
                }
                else{
                    // cout << nums[i] << nums[left] << nums[right] << endl;
                    result.push_back(vector<int>{nums[i], nums[left], nums[right]});
                    left++;
                    right--;
                    while (left < right && nums[left] == nums[left-1]){
                        left++;
                    }
                    while (left < right && nums[right] == nums[right+1]){
                        right--;
                    }
                }
            }
        }
        return result;
    }
};