/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == p || root == q || !root) return root;
        int val1 = p->val;
        int val2 = q->val;
        int cur_val = root->val;
        if (cur_val > val1 && cur_val > val2) return lowestCommonAncestor(root->left, p, q);
        if (cur_val < val1 && cur_val < val2) return lowestCommonAncestor(root->right, p, q);
        return root;
    }
};