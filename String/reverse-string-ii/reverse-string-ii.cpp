class Solution {
public:
    string reverseStr(string s, int k) {
        int n = s.size();
        int offset = 0;
        while (n - 2*k >= 0){
            for (int i = offset; i < offset + k/2; i++){
                char temp = s[i];
                s[i] = s[offset+k-1-i+offset];
                s[offset+k-1-i+offset] = temp;
            }
            n -= 2*k;
            offset += 2*k;
        }
        if (n >= k){
            for (int i = offset; i < offset + k/2; i++){
                char temp = s[i];
                s[i] = s[offset+k-1-i+offset];
                s[offset+k-1-i+offset] = temp;
            }
        }
        else {
            for (int i = offset; i < offset + n/2; i++){
                char temp = s[i];
                s[i] = s[offset+n-1-i+offset];
                s[offset+n-1-i+offset] = temp;
            }
        }
        return s;
    }
};