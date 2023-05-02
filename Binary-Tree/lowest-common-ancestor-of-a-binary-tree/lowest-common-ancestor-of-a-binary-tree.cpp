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
    TreeNode* ans;

    bool traverse(TreeNode* cur, TreeNode* p, TreeNode* q) {
        if (!cur) return false;
        bool left = false;
        bool right = false;
        if (cur->val == p->val || cur->val == q->val) {
            if (traverse(cur->left, p, q) || traverse(cur->right, p, q)) {
                ans = cur;
            }
            return true;
        }
        else {
            left = traverse(cur->left, p, q);
            right = traverse(cur->right, p, q);
            if (left && right) {
                ans = cur;
                return true;
            }
            else if (left || right) return true;
            return false;
        }

    }

    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        traverse(root, p, q);
        return ans;
    }
};