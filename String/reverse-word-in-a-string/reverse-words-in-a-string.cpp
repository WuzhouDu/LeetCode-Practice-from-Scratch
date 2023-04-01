class Solution {
public:
    string removeWhiteSpace(string s){
        int slow = 0;
        int fast = 0;

        // remove the spaces before the first word.
        while (s[fast] == ' ' && s[fast+1] == s[fast]){
            fast++;
        }
        if (s[fast] == ' ') fast++;

        // remove the extra spaces between the words
        while (fast < s.size() - 1){
            if (s[fast] != ' ' || (s[fast] == ' ' && s[fast+1] != ' ')){
                s[slow++] = s[fast++];
            }
            else fast++;
        }
        if (s[s.size() - 1] != ' '){
            s[slow++] = s[s.size() - 1];
        }
        s.resize(slow);
        return s;
    }

    string reverseALL(string s){
        for (int i = 0; i < s.size() / 2; i++){
            char temp = s[i];
            s[i] = s[s.size() - i - 1];
            s[s.size() - i - 1] = temp;
        }
        return s;
    }

    string reverseWords(string s) {
        s = removeWhiteSpace(s);
        s = reverseALL(s);
        cout << s;
        int fast = 0;
        int slow = 0;
        while (fast < s.size() - 1){
            if (s[fast] != ' '){
                fast++;
            }
            else {
                fast++;
                int word_len = fast - slow - 1;
                for (int i = 0; i < word_len/2; i++){
                    char temp = s[slow+i];
                    s[slow+i] = s[fast-2-i];
                    s[fast-2-i] = temp;
                }
                slow = fast;
            }
        }
        int word_len = fast - slow + 1;
        for (int i = 0; i < word_len/2; i++){
            char temp = s[slow + i];
            s[slow+i] = s[fast-i];
            s[fast-i] = temp;
        }
        return s;
    }
};