class Solution {
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        unordered_map<int, int> oneSumTwo;
        int result = 0;
        int n = nums4.size();
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                if (oneSumTwo.find(nums1[i] + nums2[j]) == oneSumTwo.end()){
                    oneSumTwo[nums1[i] + nums2[j]] = 1;
                }
                else {
                    oneSumTwo[nums1[i] + nums2[j]]++;
                }
            }
        }
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                if (oneSumTwo.find(-nums3[i]-nums4[j]) != oneSumTwo.end()){
                    result += oneSumTwo[-nums3[i]-nums4[j]];
                }
            }
        }
        return result;
    }
};