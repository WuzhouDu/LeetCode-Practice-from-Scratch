class Solution {
public:
    void backtrack(vector<int>& nums, vector<vector<int>>& result, vector<int>& path, int start) {
        // if (!path.empty()) cout << path.back() << endl;
        // cout << "size=" << path.size() << endl;
        
        if (path.size() >= 2) {
            result.push_back(path);
        }
        if (start >= nums.size()) return;
        for (int i = start; i < nums.size(); i++) {
            if (i > start && nums[i] == nums[i-1]) continue;
            if (path.empty() || nums[i] >= path.back()) {
                path.push_back(nums[i]);
                backtrack(nums, result, path, i+1);
                path.pop_back();
            }
        }
    }


    vector<vector<int>> findSubsequences(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> path;
        backtrack(nums, result, path, 0);
        return result;
    }
};