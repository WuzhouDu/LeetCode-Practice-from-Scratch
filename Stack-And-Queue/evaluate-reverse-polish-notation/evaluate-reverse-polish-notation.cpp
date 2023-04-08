class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stk;
        string plus = "+";
        string minus = "-";
        string times = "*";
        string subtract = "/";
        int result = 0;
        for (int i = 0; i < tokens.size(); i++){
            if ((tokens[i] != plus) && (tokens[i] != minus) && (tokens[i] != times) && (tokens[i] != subtract)){
                cout << tokens[i] << endl;
                stk.push(stoi(tokens[i]));
            }
            else {
                int num1 = stk.top();
                stk.pop();
                int num2 = stk.top();
                stk.pop();
                switch (tokens[i][0]){
                    case '+': stk.push(num1+num2); break;
                    case '-': stk.push(num2-num1); break;
                    case '*': stk.push(num1*num2); break;
                    case '/': stk.push(num2/num1); break;
                    default: cout << "invalid" << endl;
                }
            }
        }
        if (stk.size() == 1){
            return stk.top();
        }
        return 0;
    }
};