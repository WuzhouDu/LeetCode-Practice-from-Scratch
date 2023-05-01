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
    TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
        if (!root1 && !root2) return nullptr;
        if (root1 && !root2) return root1;
        if (!root1 && root2) return root2;
        int new_val = root2->val + root1->val;
        TreeNode* cur = new TreeNode(new_val);
        cur->left = mergeTrees(root1->left, root2->left);
        cur->right = mergeTrees(root1->right, root2->right);
        return cur;
    }
};