/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    unordered_map<int, int> hash;
    TreeNode* build(int left, int right, vector<int>& nums){
        if (left > right) return nullptr;
        if (left == right) return new TreeNode(nums[left]);
        int max = -1;
        int max_index = -1;
        for (int i = left; i <= right; i++){
            if (nums[i] > max){
                max = nums[i];
                max_index = i;
            }
        }
        if (max == -1) cout << "Error" << endl;
        TreeNode* cur = new TreeNode(max);
        cur->left = build(left, max_index-1, nums);
        cur->right = build(max_index+1, right, nums);
        return cur;
    }

    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        return build(0, nums.size()-1, nums);
    }
};