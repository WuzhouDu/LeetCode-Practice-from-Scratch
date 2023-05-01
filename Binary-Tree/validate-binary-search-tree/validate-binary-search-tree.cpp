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
    bool isValidBST(TreeNode* root) {
        if (!root) return true;
        if (!root->left && !root->right) return true;
        bool left = isValidBST(root->left);
        if (!left) return false;
        bool right = isValidBST(root->right);
        if (!right) return false;
        TreeNode* cur = root->left;
        while (cur){
            if (cur->val >= root->val) return false;
            cur = cur->right;
        }
        cur = root->right;
        while (cur){
            if (cur->val <= root->val) return false;
            cur = cur->left;
        }
        return true;
    }
};
