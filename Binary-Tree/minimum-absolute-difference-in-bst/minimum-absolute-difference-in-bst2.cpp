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
    int answer = INT_MAX;
    int pre = -1;
    void traverse(TreeNode* root) {
        if (!root) return;
        traverse(root->left);
        if (pre == -1) {
            pre = root->val;
        }
        else {
            answer = min(abs(root->val - pre), answer);
            pre = root->val;
        }
        traverse(root->right);
    }

    int getMinimumDifference(TreeNode* root) {
        traverse( root);
        return answer;
    }
};