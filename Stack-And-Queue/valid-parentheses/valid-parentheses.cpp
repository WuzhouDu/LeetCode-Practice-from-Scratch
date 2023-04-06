class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        for (int i = 0; i < s.size(); i++){
            if (s[i] == '(' || s[i] == '[' || s[i] == '{'){
                stk.push(s[i]);
            }
            else{
                if (stk.empty()) return false;
                char top = stk.top();
                stk.pop();
                switch (s[i]){
                    case ')': if (top != '(') {
                        return false;
                    }
                    else break;
                    case ']': if (top != '[') {
                        return false;
                    }
                    else break;
                    case '}': if (top != '{') {
                        return false;
                    }
                    else break;
                }
            }
        }
        if (stk.empty()) return true;
        else return false;
    }
};