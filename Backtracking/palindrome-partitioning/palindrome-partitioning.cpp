class Solution {
public:
    bool isPalindrome(string s) {
        if (s == "") return false;
        int size = s.size();
        for (int i = 0; i < size/2; i++) {
            if (s[i] != s[size-1-i]) return false;
        }
        return true;
    }


    void backtrack(string s, vector<vector<string>> &result, string path, vector<string> &temp, int cur) {
        if (cur == s.size()-1) {
            if (isPalindrome(path+s[cur])) {
                temp.push_back(path+s[cur]);
                result.push_back(temp);
                temp.pop_back();
                return;
            }
            return;
        }
        
        if (isPalindrome(path+s[cur])) {
            temp.push_back(path+s[cur]);
            backtrack(s, result, "", temp, cur+1);
            temp.pop_back();
        }
        backtrack(s, result, path+s[cur], temp, cur+1);

    }


    vector<vector<string>> partition(string s) {
        vector<vector<string>> result;
        vector<string> temp;
        backtrack(s, result, "", temp, 0);
        return result;
    }
};