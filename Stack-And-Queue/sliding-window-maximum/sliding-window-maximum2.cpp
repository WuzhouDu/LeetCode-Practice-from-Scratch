class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> result(nums.size()-k+1);
        deque<int> q;
        for (int i = 0; i < k; ++i){
            while (!q.empty() && q.back() < nums[i]){
                q.pop_back();
            }
            q.push_back(nums[i]);
        }
        result[0] = q.front();
        for (int i = 1; i < result.size(); i++){
            if (!q.empty() && q.front() == nums[i-1]) q.pop_front();
            while (!q.empty() && q.back() < nums[i+k-1]){
                q.pop_back();
            }
            q.push_back(nums[i+k-1]);
            result[i] = q.front();
        }
        return result;
    }
};
