class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> result;
        if (nums.size() < 4) return result;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size()-3; i++){
            if (nums[i] >= 0 && nums[i] > target) break;
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }
            for (int j = i+1; j < nums.size()-2; j++){
                if (nums[i] + nums[j] >= 0 && nums[i] + nums[j] > target) break;
                if ( j > i+1 && nums[j] == nums[j-1]) continue;
                int left = j + 1;
                int right = nums.size() - 1;
                while (left < right){
                    if (nums[i] + nums[j] < target - nums[left] - nums[right]){
                        left++;
                    }
                    else if (nums[i] + nums[j] > target - nums[left] - nums[right]){
                        right--;
                    }
                    else {
                        result.push_back(vector<int>{nums[i], nums[j], nums[left], nums[right]});
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
        }
        return result;
    }
};