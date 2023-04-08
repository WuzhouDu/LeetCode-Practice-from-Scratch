class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        queue<int> q;
        vector<int> result(nums.size()-k+1);
        int max = INT_MIN;
        for (int i = 0; i < k; i++){
            q.push(nums[i]);
            if (nums[i] > max) max = nums[i];
        }
        result[0] = max;
        for (int i = 1; i < result.size(); i++){
            if (nums[i+k-1] >= max){
                max = nums[i+k-1];
                result[i] = max;
                q.pop();
                q.push(nums[i+k-1]);
            }
            else{
                if (q.front() < max){
                    result[i] = max;
                    q.pop();
                    q.push(nums[i+k-1]);
                }
                else {
                    q.pop();
                    q.push(nums[i+k-1]);
                    max = nums[i+k-1];
                    for (int j = 0; j < k; j++){
                        if (nums[i+j] > max) max = nums[i+j];
                    }
                    result[i] = max;
                }
            }
        }
        return result;
    }
};