class Solution {
public:
    void backtrack(vector<int>& candidates, vector<vector<int>> &result, vector<int> &path, int target, int start) {
        if (target == 0) {
            result.push_back(path);
            return;
        }

        for (int i = start; i < candidates.size(); i++) {
            if (target >= candidates[i]) {
                path.push_back(candidates[i]);
                backtrack(candidates, result, path, target - candidates[i], i);
                path.pop_back();
            }
        }
    }


    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> path;
        backtrack(candidates, result, path, target, 0);
        return result;
    }
};