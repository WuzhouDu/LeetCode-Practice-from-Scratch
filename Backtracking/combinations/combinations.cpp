class Solution {
public:
    void backtrack(int begin, int n, int k, vector<vector<int>> &result, vector<int> &temp) {
        if (temp.size() == k) {
            result.push_back(temp);
            return;
        }

        for (int i = begin; i <= n; i++) {
            temp.push_back(i);
            backtrack(i+1, n, k, result, temp);
            temp.pop_back();
        }
    }

    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> result;
        vector<int> temp;
        backtrack(1, n, k, result, temp);
        return result;
    }
};