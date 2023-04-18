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
    int getHeight(TreeNode* root){
        if (root == nullptr) return 0;
        int left = getHeight(root->left);
        if (left == -1) return -1;
        int right = getHeight(root->right);
        if (right == -1) return -1;
        if (abs(left - right) <= 1) return max(left, right) + 1;
        return -1;
    }

    bool isBalanced(TreeNode* root) {
        if (root == nullptr) return true;
        return getHeight(root) == -1 ? false : true;
    }
};