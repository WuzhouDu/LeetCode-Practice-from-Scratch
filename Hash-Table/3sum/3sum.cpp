class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        unordered_map<int, unordered_set<unordered_set<int>>> hash;
        vector<vector<int>> result;
        for (int i = 0; i < nums.size(); i++){
            for (int j = i; j < nums.size(); j++){
                unordered_set<int> temp {i, j};
                hash[nums[i] + nums[j]].insert(temp);
            }
        }

        for (int i = 0; i < nums.size(); i++){
            if (hash.find(0-nums[i]) != hash.end()){
                for (auto it = hash[0-nums[i]].begin(); it != hash[0-nums[i]].end(); it++){
                    if ((*it).find(i) == (*it).end()){
                        vector<int> temp;
                        temp.assign((*it).begin(), (*it).end());
                        temp.push_back(i);
                        result.push_back(temp);
                    }
                }
            }
        }
        return result;
    }
};