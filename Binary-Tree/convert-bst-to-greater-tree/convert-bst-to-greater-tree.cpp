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
    int now = 0;
    TreeNode* convertBST(TreeNode* root) {
        if (!root) return root;
        convertBST(root->right);
        now += root->val;
        root->val = now;
        convertBST(root->left);
        return root;
    }
};