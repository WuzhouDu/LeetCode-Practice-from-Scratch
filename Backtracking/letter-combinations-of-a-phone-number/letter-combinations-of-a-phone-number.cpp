class Solution {
public:
    void backtrack(string digits, int cur, vector<string> &result, string &temp) {
        if (cur == digits.size()) {
            result.push_back(temp);
            return;
        }

        switch (digits[cur]) {
            case '2': 
                temp.push_back('a');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                temp.push_back('b');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                temp.push_back('c');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                break;
            case '3':
                temp.push_back('d');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                temp.push_back('e');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                temp.push_back('f');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                break;      
            case '4':
                temp.push_back('g');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                temp.push_back('h');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                temp.push_back('i');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                break;
            case '5':
                temp.push_back('j');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                temp.push_back('k');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                temp.push_back('l');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                break;
            case '6':
                temp.push_back('m');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                temp.push_back('n');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                temp.push_back('o');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                break;
            case '7':
                temp.push_back('p');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                temp.push_back('q');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                temp.push_back('r');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                temp.push_back('s');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                break;
            case '8':
                temp.push_back('t');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                temp.push_back('u');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                temp.push_back('v');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                break;
            case '9':
                temp.push_back('w');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                temp.push_back('x');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                temp.push_back('y');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                temp.push_back('z');
                backtrack(digits, cur+1, result, temp);
                temp.pop_back();
                break;
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