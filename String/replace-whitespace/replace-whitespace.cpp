class Solution {
public:
    string replaceSpace(string s) {
        int ws_num = 0;
        int old_size = s.size();
        for (int i = 0; i < s.size(); i++){
            if (s[i] == ' ') ws_num++;
        }
        s.resize(s.size() + 2*ws_num);
        int new_size = s.size();
        for (int i = new_size-1, j = old_size-1; i >= 0; j--){
            if (s[j] != ' '){
                s[i] = s[j];
                i--;
            }
            else {
                s[i] = '0';
                s[i-1] = '2';
                s[i-2] = '%';
                i -= 3;
            }
        }
        return s;
    }
};