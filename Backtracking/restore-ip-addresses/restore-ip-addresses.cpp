class Solution {
public:
    void backtrack(string s, int start, int pointNum, string temp, vector<string> &result) {
        if (start >= s.size()) return;
        if (pointNum == 3) {
            string sub = s.substr(start, s.size() - start);
            if (sub == "") return;
            if (s[start] == '0') {
                if (sub == "0") {
                    result.push_back(temp);
                    return;
                }
                else return;
            }
            if (stoll(sub) <= 255) {
                result.push_back(temp);
            }
            return;
        }

        if (s[start] == '0') {
            backtrack(s, start+1, pointNum+1, temp.insert(start+1+pointNum, "."), result);
            temp.erase(start+1+pointNum);
            return;
        }        

        for (int i = start; i < start+3 && i < s.size(); i++) {
            string sub = s.substr(start, i - start+1);
            if (stoll(sub) <= 255) {
                backtrack(s, i+1, pointNum+1, temp.insert(i+1+pointNum, "."), result);
                temp.erase(temp.begin()+i+1+pointNum);
            }
        }
    }


    vector<string> restoreIpAddresses(string s) {
        vector<string> result;
        backtrack(s, 0, 0, s, result);
        return result;
    }
};