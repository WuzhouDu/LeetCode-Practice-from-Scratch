class Solution {
public:
    void backtrack(vector<int>& nums, vector<vector<int>> &result, vector<int> &temp, int start) {
        // cout << start << endl;
        if (start >= nums.size()) {
            result.push_back(temp);
            return;
        }

        temp.push_back(nums[start]);
        backtrack(nums, result, temp, start+1);
        temp.pop_back();
        backtrack(nums, result, temp, start+1);

    }


    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> temp;
        backtrack(nums, result, temp, 0);
        return result;
    }
};