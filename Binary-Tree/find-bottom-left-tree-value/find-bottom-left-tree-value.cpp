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
    int findBottomLeftValue(TreeNode* root) {
        int result;
        if (!root->left && !root->right) return root->val;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()){
            int level_size = q.size();
            for (int i = 0; i < level_size; ++i){
                TreeNode* cur = q.front();
                q.pop();
                if (i == 0) result = cur->val;
                if (cur->left) q.push(cur->left);
                if (cur->right) q.push(cur->right);
            }
        }
        return result;
    }
};