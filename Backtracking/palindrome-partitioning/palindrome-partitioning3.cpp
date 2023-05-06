class Solution {
public:
    // bool isPalindrome(string s) {
    //     if (s == "") return false;
    //     int size = s.size();
    //     for (int i = 0; i < size/2; i++) {
    //         if (s[i] != s[size-1-i]) return false;
    //     }
    //     return true;
    // }
    vector<vector<bool>> isPalindrome;


    void backtrack(string s, vector<vector<string>> &result, vector<string> &path, int cur) {
        if (cur == s.size()) {
            result.push_back(path);
            return;
        }

        for (int i = cur; i < s.size(); i++) {
            string temp = s.substr(cur, i - cur + 1);
            if (isPalindrome[cur][i]) {
                path.push_back(temp);
                backtrack(s, result, path, i+1);
                path.pop_back();
            }
        }

    }

    vector<vector<string>> partition(string s) {
        vector<vector<string>> result;
        vector<string> path;
        isPalindrome.resize(s.size(), vector<bool>(s.size(), false));
        for (int i = s.size()-1; i >= 0; i--) {
            for (int j = i; j < s.size(); j++) {
                if (j == i) isPalindrome[i][j] = true;
                else if (j - i == 1) isPalindrome[i][j] = s[i] == s[j];
                else isPalindrome[i][j] = isPalindrome[i+1][j-1] && s[i] == s[j];
            }
        }
        backtrack(s, result, path, 0);
        return result;
    }
};