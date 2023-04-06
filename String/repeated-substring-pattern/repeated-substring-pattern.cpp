class Solution {
public:
    void getNext(string s, int* next){
        next[0] = 0;
        int j = 0;
        for (int i = 1; i < s.size(); i++){
            while (j > 0 && s[i] != s[j]){
                j = next[j-1];
            }
            if (s[i] == s[j]){
                j++;
                next[i] = j;
            }
            else{
                next[i] = 0;
            }
        }
    }

    bool repeatedSubstringPattern(string s) {
        string t = s+s;
        int next[t.size()];
        getNext(t, next);
        // for (int i = 0; i < t.size(); i++){
        //     cout << next[i];
        // }
        // cout << endl;
        int j = 0;
        for (int i = 1; i < t.size() - 1; i++){

            while (j > 0 && t[i] != s[j]){
                j = next[j-1];
            }

            if (t[i] == s[j]){
                j++;
            }
            // cout << j << endl;
            if (j == s.size()){
                return true;
            }
        }
        return false;
    }
};