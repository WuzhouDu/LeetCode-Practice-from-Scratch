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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        queue<TreeNode*> q;
        if (root == nullptr) return result;
        q.push(root);
        while (!q.empty()){
            vector<int> temp;
            int size = q.size();
            for (int i = 0; i < size; i++){
                TreeNode* cur = q.front();
                temp.push_back(cur->val);
                q.pop();
                if (cur->left != nullptr) q.push(cur->left);
                if (cur->right != nullptr) q.push(cur->right);
            }
            result.push_back(temp);
        }
        return result;
    }
};