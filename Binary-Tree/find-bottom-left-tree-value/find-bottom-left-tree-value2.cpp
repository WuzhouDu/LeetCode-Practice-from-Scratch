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
    int result;
    int max_depth = -1;
    void traverse(TreeNode* cur, int depth) {
        if (!cur->left && !cur->right) {
            if (depth > max_depth){
                max_depth = depth;
                result = cur->val;
            }
        };
        if (cur->left) traverse(cur->left, depth+1);
        if (cur->right) traverse(cur->right, depth+1);
    }

    int findBottomLeftValue(TreeNode* root) {
        if (root) {
            traverse(root, 0);
            return result;
        }
        else return 0;
    }
};