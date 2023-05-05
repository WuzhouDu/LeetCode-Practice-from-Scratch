class Solution {
public:
    string map[10] = {
        "",
        "",
        "abc",
        "def",
        "ghi",
        "jkl",
        "mno",
        "pqrs",
        "tuv",
        "wxyz"
    };

    void backtrack(string digits, int cur, vector<string> &result, string &temp) {
        if (cur == digits.size()) {
            result.push_back(temp);
            return;
        }

        int digit = digits[cur] - '0';
        for (int i = 0; i < map[digit].size(); i++) {
            temp += map[digit][i];
            backtrack(digits, cur+1, result, temp);
            temp.pop_back();
        }
    }

    vector<string> letterCombinations(string digits) {
        vector<string> result;
        string temp;
        if (digits.size() == 0) return result;
        backtrack(digits, 0, result, temp);
        return result;
    }
};