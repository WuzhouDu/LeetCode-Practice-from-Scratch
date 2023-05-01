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
    bool helper(long long upperbound, long long lowerbound, TreeNode*root) {
        if (!root) return true;
        if (root->val >= upperbound || root->val <= lowerbound) return false;
        bool left = helper(root->val, lowerbound, root->left);
        if (!left) return false;
        bool right = helper(upperbound, root->val, root->right);
        return right;
    }

    bool isValidBST(TreeNode* root) {
        return helper(LONG_MAX, LONG_MIN, root);
    }
};