class Solution {
public:
    void getPrefix(string s, int* array){
        array[0] = 0;
        int j = 0;
        for (int i = 1; i < s.size(); i++){
            while (j > 0 && s[j] != s[i]){
                j = array[j-1];
            }
            if (s[j] == s[i]) j++;
            array[i] = j;
        }
    }


    int strStr(string haystack, string needle) {
        int next[needle.size()];
        getPrefix(needle, next);
        int i = 0;
        int j = 0;
        while (j < needle.size() && i < haystack.size()){
            if (haystack[i] == needle[j]){
                i++;
                j++;
            }
            else{
                while (j > 0 && haystack[i] != needle[j]){
                    j = next[j-1];
                }
                if (j == 0 && haystack[i] != needle[j]) i++;
            }
        }
        if (j == needle.size()) return i - j;
        else return -1;
    }
};