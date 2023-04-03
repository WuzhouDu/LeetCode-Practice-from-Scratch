class Solution {
public:
    void reverseString(string &s, int n){
        for (int i = 0; i < n / 2; i++){
            char temp = s[i];
            s[i] = s[n - 1 - i];
            s[n - 1 - i] = temp;
        }
    }

    string reverseLeftWords(string s, int n) {
        reverseString(s, n);
        reverseString(s, s.size());
        reverseString(s, s.size() - n);
        return s;
    }
};