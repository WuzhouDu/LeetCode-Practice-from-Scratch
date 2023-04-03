class Solution {
public:
    string reverseLeftWords(string s, int n) {
        int slow = 0;
        string temp;
        for (int i = 0; i < n; i++){
            temp += s[i];
        }
        for (; slow < s.size(); slow++){
            if (slow < s.size() - n){
                s[slow] = s[slow+n];
            }
            else {
                s[slow] = temp[slow-s.size()+n];
            }
        }
        return s;
    }
};