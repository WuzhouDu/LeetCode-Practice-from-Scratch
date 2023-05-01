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
    TreeNode* build(int pre_begin, int pre_end, int post_begin, int post_end, vector<int>& preorder, vector<int>& postorder){
        if (pre_begin > pre_end) return nullptr;
        if (pre_begin == pre_end) return new TreeNode(preorder[pre_begin]);
        TreeNode* cur = new TreeNode(preorder[pre_begin]);
        int left_pivot = preorder[pre_begin+1];
        int left_pre_begin = pre_begin+1;
        int left_post_end = hash[left_pivot];
        int left_post_begin = post_begin;
        int left_pre_end = left_post_end - left_post_begin + left_pre_begin;
        cur->left = build(left_pre_begin, left_pre_end, left_post_begin, left_post_end, preorder, postorder);
        int right_pre_begin = left_pre_end+1;
        int right_pre_end = pre_end;
        int right_post_begin = left_post_end+1;
        int right_post_end = post_end-1;
        cur->right = build(right_pre_begin, right_pre_end, right_post_begin, right_post_end, preorder, postorder);
        return cur;

    }


    TreeNode* constructFromPrePost(vector<int>& preorder, vector<int>& postorder) {
        if (preorder.size() == 0) return nullptr;
        for (int i = 0; i < postorder.size(); i++){
            hash[postorder[i]] = i;
        }
        return build(0, preorder.size()-1, 0, postorder.size()-1, preorder, postorder);
    }
};