class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        vector<int> table(26, 0);
        for (int i = 0; i < s.size(); i++){
            table[s[i] - 'a']++;
        }
        for (int i = 0; i < t.size(); i++){
            table[t[i] - 'a']--;
        }
        for (int i = 0; i < table.size(); i++){
            if (table[i] != 0) return false;
        }
        return true;
    }
};