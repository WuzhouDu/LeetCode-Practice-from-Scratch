class Solution {
public:
    void backtrack(vector<vector<int>>& result, vector<int>& nums, vector<int>& path, int start) {
        result.push_back(path);
        if (start >= nums.size()) return;

        for (int i = start; i < nums.size(); i++) {
            if (i > start && nums[i] == nums[i-1]) continue;
            path.push_back(nums[i]);
            backtrack(result, nums, path, i+1);
            path.pop_back();
        }
    }

    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> path;
        sort(nums.begin(), nums.end());
        backtrack(result, nums, path, 0);
        return result;
    }
};