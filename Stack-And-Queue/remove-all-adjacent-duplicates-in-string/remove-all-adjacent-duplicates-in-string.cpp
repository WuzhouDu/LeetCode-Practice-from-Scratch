class Solution {
public:
    string removeDuplicates(string s) {
        stack<char> stk;
        stack<char> temp;
        string result;
        for (int i = 0; i < s.size(); i++){
            if (stk.empty()) stk.push(s[i]);
            else if (stk.top() == s[i]) {
                stk.pop();
            }
            else stk.push(s[i]);
        }
        while (!stk.empty()){
            char a = stk.top();
            stk.pop();
            temp.push(a);
        }
        while (!temp.empty()){
            result += temp.top();
            temp.pop();
        }
        return result;
    }
};