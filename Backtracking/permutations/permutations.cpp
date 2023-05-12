class Solution {
public:
    vector<bool> map;
    void backtrack(vector<int>& nums, vector<int>& path, vector<vector<int>>& result) {
        if (path.size() == nums.size()) {
            result.push_back(path);
            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            if (map[i]) continue;
            map[i] = true;
            path.push_back(nums[i]);
            backtrack(nums, path, result);
            path.pop_back();
            map[i] = false;
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        map.resize(nums.size(), false);
        vector<vector<int>> result;
        vector<int> path;
        backtrack(nums, path, result);
        return result;
    }
};