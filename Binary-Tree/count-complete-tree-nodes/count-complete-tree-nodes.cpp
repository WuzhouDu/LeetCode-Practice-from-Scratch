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
    int countNodes(TreeNode* root) {
        if (root == nullptr) return 0;
        int leftDepth = 0;
        int rightDepth = 0;
        TreeNode* cur = root;
        while (cur->left){
            ++leftDepth;
            cur = cur->left;
        }
        while (cur->right){
            ++rightDepth;
            cur = cur->right;
        }
        if (leftDepth == rightDepth) return (2 << leftDepth) - 1;
        else {
            return countNodes(root->left) + countNodes(root->right) + 1;
        }
    }
};