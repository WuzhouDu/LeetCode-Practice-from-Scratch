class Solution {
public:
    void backtrack(vector<int>& nums, vector<vector<int>>& result, vector<int>& path, int start, vector<int>& bit_vec) {
        // if (!path.empty()) cout << path.back() << endl;
        // cout << "size=" << path.size() << endl;
        
        if (path.size() >= 2) {
            result.push_back(path);
        }
        if (start >= nums.size()) return;
        for (int i = start; i < nums.size(); i++) {
            bool brek = false;
            for (int j = start; j < i; j++) {
                if (nums[j] == nums[i] && bit_vec[j] == 0) {
                    brek = true;
                    break;
                }
            }
            if (brek) continue;
            if (path.empty() || nums[i] >= path.back()) {
                bit_vec[i] = 1;
                path.push_back(nums[i]);
                backtrack(nums, result, path, i+1, bit_vec);
                path.pop_back();
                bit_vec[i] = 0;
            }
        }
    }


    vector<vector<int>> findSubsequences(vector<int>& nums) {
        vector<int> bit_vec(nums.size(), 0);
        vector<vector<int>> result;
        vector<int> path;
        backtrack(nums, result, path, 0, bit_vec);
        return result;
    }
};