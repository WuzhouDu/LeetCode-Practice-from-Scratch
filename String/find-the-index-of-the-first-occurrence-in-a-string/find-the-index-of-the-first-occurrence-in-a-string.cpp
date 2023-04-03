class Solution {
public:
    int strStr(string haystack, string needle) {
        if (haystack.size() < needle.size()) return -1;
        for (int i = 0; i < haystack.size() - needle.size()+1; i++){
            if (haystack[i] != needle[0]) continue;
            else{
                bool find = 1;
                for (int j = 0; j < needle.size(); j++){
                    if (haystack[i+j] != needle[j]){
                        find = 0;
                        break;
                    }
                }
                if (find) return i;
            }
        }
        return -1;
    }
};