class Solution {
public:
    void backtrack(int k, int n, vector<vector<int>> &result, vector<int> &temp, int current) {
        if (temp.size() == k && n == 0) {
            result.push_back(temp);
            return;
        }

        if (n < current) return;
        for (int i = current; i <= min(n, 9); i++) {
            temp.push_back(i);
            backtrack(k, n - i, result, temp, i+1);
            temp.pop_back();
        }
    }


    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> result;
        vector<int> temp;
        backtrack(k, n, result, temp, 1);
        return result;
    }
};